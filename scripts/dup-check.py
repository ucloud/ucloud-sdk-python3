#!/usr/bin/env python3
"""G2 重复闸 —— python 生成代码重复声明检测。

背景：`python -m compileall` 对同一模块内重复的 class/def 一律 exit 0
（Python 语义上是后者覆盖前者，不是语法错误），故编译器闸抓不住这类缺陷。
本脚本用 stdlib 的 ast 补上，零额外依赖。

检测三类：
  1. 模块顶层重复的 class / def 名
  2. 类体内重复的方法名
  3. 重复的 import 别名（from x import Y 出现多次同名 Y）

用法：
  dup-check.py <目录|文件> [...]
      全部命中都阻断。本地开发和 CI 的退回路径走这条。
  dup-check.py --strict-list <清单文件> <目录|文件> [...]
      **仍然全量扫描**，但只有清单内文件的命中才阻断，其余降为告警。
      清单文件每行一个路径（相对当前目录或绝对均可），空行忽略。

为什么要分级：仓里有存量的幽灵重复（uphost 的 get_phost_disk_upgrade_price），
整棵树一律阻断会让**任何**产品的 codegen PR 被这处无关问题判红，自动合并永久失效。
完整推理与判定边界见 scripts/ci-syntax.sh 文件头。

退出码：0 = 阻断级命中为 0；1 = 有阻断级命中，或参数/路径有误
"""
import argparse
import pathlib
import ast
import sys


def dup_names(nodes, kinds):
    seen = {}
    for n in nodes:
        if isinstance(n, kinds):
            seen.setdefault(n.name, []).append(n.lineno)
    return {k: v for k, v in seen.items() if len(v) > 1}


DEF_KINDS = (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
FUNC_KINDS = (ast.FunctionDef, ast.AsyncFunctionDef)


def check(path):
    findings = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        # 语法错误归 G1 编译器闸管，这里只记录不重复判定
        findings.append("%s:%s 语法错误（应由 G1 拦截）：%s" % (path, exc.lineno, exc.msg))
        return findings

    for name, lines in dup_names(tree.body, DEF_KINDS).items():
        findings.append("%s:%s 顶层重复声明 '%s'" % (path, ",".join(map(str, lines)), name))

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for name, lines in dup_names(node.body, FUNC_KINDS).items():
                findings.append(
                    "%s:%s 类 '%s' 内重复方法 '%s'"
                    % (path, ",".join(map(str, lines)), node.name, name)
                )

    # 只看**模块顶层**的 import。嵌在 if / try 里的是条件导入，
    # 同名出现在不同分支是标准的版本兼容写法，不是重复。
    # 实例：ucloud/core/utils/compat.py 用 `if PY3: from collections.abc import Callable
    # else: from collections import Callable` —— 用 ast.walk 会误判为重复。
    aliases = {}
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                key = alias.asname or alias.name
                aliases.setdefault(key, []).append(node.lineno)
    for name, lines in aliases.items():
        if len(lines) > 1:
            findings.append("%s:%s 重复导入 '%s'" % (path, ",".join(map(str, lines)), name))

    return findings


def norm(path):
    """统一成绝对路径再比对：清单来自 git（仓库根相对路径），扫描结果来自 rglob
    （命令行给的 root 相对路径），两边的字面量对不上，只有归一化后才可靠。"""
    return str(pathlib.Path(path).resolve())


def iter_py_files(root):
    """root 可以是目录（递归取 *.py）也可以是单个 .py 文件——后者是为了让调用方
    能直接传变更文件清单，不必先反推目录。"""
    p = pathlib.Path(root)
    if p.is_dir():
        return sorted(p.rglob("*.py"))
    if p.is_file():
        return [p] if p.suffix == ".py" else []
    return None  # 不存在：由调用方 fail-closed 处理，不能当成「扫过且没问题」


def load_strict_set(list_path):
    p = pathlib.Path(list_path)
    if not p.is_file():
        return None
    return {norm(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()}


def main(argv):
    parser = argparse.ArgumentParser(
        description="python 生成代码重复声明检测（G2 重复闸）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--strict-list",
        metavar="清单文件",
        help="每行一个路径；只有清单内文件的命中才阻断，其余降为告警。不给则全部阻断。",
    )
    parser.add_argument("roots", nargs="*", default=None, help="要扫描的目录或 .py 文件")
    args = parser.parse_args(argv[1:])

    roots = args.roots or ["ucloud"]

    strict_set = None
    if args.strict_list is not None:
        strict_set = load_strict_set(args.strict_list)
        if strict_set is None:
            # 读不到清单就当「什么都不阻断」是静默放行，与 fail-closed 相悖，直接报错。
            print("G2 重复闸：--strict-list 指向的文件不存在：%s" % args.strict_list)
            return 1

    strict, advisory = [], []
    scanned = 0
    for root in roots:
        paths = iter_py_files(root)
        if paths is None:
            print("G2 重复闸：路径不存在，无法扫描：%s" % root)
            return 1
        for path in paths:
            scanned += 1
            findings = check(path)
            if not findings:
                continue
            if strict_set is None or norm(path) in strict_set:
                strict.extend(findings)
            else:
                advisory.extend(findings)

    if advisory:
        print("G2 重复闸 [告警]：存量文件命中 %d 处 —— 不阻断，只保持可见" % len(advisory))
        for line in advisory:
            print("  " + line)
        print("  （这些文件不在本轮变更集内，命中来自既有代码；判定边界见 scripts/ci-syntax.sh 文件头）")

    if strict:
        print("G2 重复闸 [阻断] 失败：命中 %d 处（共扫描 %d 个文件）" % (len(strict), scanned))
        for line in strict:
            print("  " + line)
        return 1

    if strict_set is None:
        print("G2 重复闸通过：%d 个文件无重复声明" % scanned)
    else:
        print(
            "G2 重复闸通过：扫描 %d 个文件；本轮变更文件 0 处命中，存量告警 %d 处"
            % (scanned, len(advisory))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
