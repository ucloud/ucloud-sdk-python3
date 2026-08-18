#!/usr/bin/env bash
# CI 语法门禁：G1 编译闸（compileall）+ G2 重复闸（dup-check.py）。由 `make ci-syntax` 调用。
#
# ── 为什么「全量扫描」和「严格判定」是两个范围 ────────────────────────────────
# 仓里躺着存量缺陷：ucloud/services/uphost/client.py 有一处重复方法
# get_phost_disk_upgrade_price——已删除 API 的旧快照被 publish 集合（追加式存储）留了
# 下来，python codegen 直读该集合就把幽灵一并生成。它改 SDK 仓库无效，根治在
# ucloud-model 侧补「编辑态已不存在则丢弃」的过滤，属独立任务。
#
# 若整棵树一律阻断，发**任何一个**产品（UDisk、UNet……）的 codegen PR 都会被这处与本次
# 发布毫无关系的存量问题判红，mergeable_state 随之变 unstable，自动合并永久失效——
# 那恰好是这套门禁要解决的问题本身。
#
# 后果 2026-07-31 已被实证并明确否决：pipeline 2507836 发的是 UHost+UAI-Modelverse、
# 根本没重新生成 uphost，那处重复照样被扫了出来，证明来源是存量代码而非本轮产物。
# 当时的处置是「判定边界取本轮变更文件，存量只告警」，落在
# ucloud-sdk-release/scripts/python-fatal-check.sh 的文件头。本脚本把同一原则落到
# GitHub Actions 上，两端同源。
#
# 存量仍然**全量扫描**：不阻断不等于不检查。债务要保持可见、可度量，否则收窄判定范围
# 就退化成了掩盖问题。
#
# ── 严格集怎么算 ────────────────────────────────────────────────────────────
# 取环境变量 CI_BASE_SHA（workflow 里 PR 事件给 base.sha、push 事件给 before）：
#   · 能解析成 commit → 严格集 = `git diff --name-only $CI_BASE_SHA...HEAD` 结果中
#     ucloud/ 下的 .py 文件。三点式取的是 merge-base 到 HEAD，正好等于本 PR 引入的改动；
#     --diff-filter=d 排除删除项，删掉的文件没法编译。
#   · 未设置 / 解析不出（force push 覆盖了原提交、新分支的全零 sha、clone 深度不够、
#     两端无共同祖先）→ 退回整棵树严格判定，并打印退回原因。
# fail-closed：拿不准就严格，绝不静默放行。本地不设该变量看到的就是整棵树严格判定，
# 与 CI 的退回路径完全一致，不引入「本地绿 / CI 红」的分叉。

# 不用 set -e：本脚本要接住 compileall / dup-check 的非零退出码自行分级判定。
set -uo pipefail

ROOT_DIR="ucloud"
MAX_LIST_ECHO=30 # 全量重生成会变更数百个文件，日志里全打出来只是噪声

if [ ! -d "$ROOT_DIR" ]; then
	echo "FATAL: 未找到 ${ROOT_DIR}/，请在仓库根目录执行（当前目录：$(pwd)）。"
	exit 1
fi

# ── 第一步：确定严格集 ───────────────────────────────────────────────────────
SUBSET_MODE=0    # 1 = 严格集是子集；0 = 严格集是整棵树
FALLBACK_REASON="" # SUBSET_MODE=0 时说明为什么退回
STRICT_FILES=()

if [ -z "${CI_BASE_SHA:-}" ]; then
	FALLBACK_REASON="未设置 CI_BASE_SHA（本地直接执行 make ci-syntax 的常态）"
elif ! git rev-parse --verify --quiet "${CI_BASE_SHA}^{commit}" >/dev/null 2>&1; then
	FALLBACK_REASON="CI_BASE_SHA=${CI_BASE_SHA} 解析不出 commit（force push 覆盖了原提交 / 新分支的全零 sha / checkout 没设 fetch-depth: 0 / 不在 git 仓库里）"
elif ! CHANGED="$(git diff --name-only --diff-filter=d "${CI_BASE_SHA}...HEAD" -- "$ROOT_DIR" 2>&1)"; then
	FALLBACK_REASON="git diff ${CI_BASE_SHA}...HEAD 执行失败（两端无共同祖先时会这样）：${CHANGED}"
else
	SUBSET_MODE=1
	while IFS= read -r f; do
		# 只收 .py；-f 兜底防止 rename/filter 之外的意外让 compileall 拿到不存在的路径
		case "$f" in
		*.py) [ -f "$f" ] && STRICT_FILES+=("$f") ;;
		esac
	done <<<"$CHANGED"
fi

echo "════ ci-syntax ════"
if [ "$SUBSET_MODE" -eq 1 ]; then
	echo "严格判定范围：本轮变更的 ${#STRICT_FILES[@]} 个文件（${CI_BASE_SHA}...HEAD 下 ${ROOT_DIR}/ 的 .py）"
	echo "全量扫描范围：整棵 ${ROOT_DIR}/（存量命中只告警，不计入退出码）"
	if [ "${#STRICT_FILES[@]}" -gt 0 ] && [ "${#STRICT_FILES[@]}" -le "$MAX_LIST_ECHO" ]; then
		printf '  %s\n' "${STRICT_FILES[@]}"
	fi
else
	echo "严格判定范围：整棵 ${ROOT_DIR}/"
	echo "退回原因：${FALLBACK_REASON}"
fi
echo

# ── 第二步：G1 编译闸 ────────────────────────────────────────────────────────
# compileall 覆盖 ucloud/ 下全部生成代码（lint 显式 --exclude 掉了 ucloud/services，
# 也就是生成代码一直没人查）。真缺陷它抓得住，实测：`def uai-modelverse(self):`
# （连字符产品名回填成非法标识符，真实事故形态）→ exit 1 SyntaxError；
# 而纯格式问题 `def  foo( a,b ):` → exit 0。这正是想要的分界线。
echo "─── G1 编译闸 [全量扫描] python -m compileall ${ROOT_DIR} ───"
python -m compileall -q "$ROOT_DIR"
g1_full=$?

if [ "$SUBSET_MODE" -eq 0 ]; then
	g1_gate=$g1_full
	if [ "$g1_full" -eq 0 ]; then
		echo "G1 通过：${ROOT_DIR}/ 全部可编译"
	else
		echo "G1 失败：整棵树严格判定，上方 *** Error compiling 即阻断项"
	fi
else
	if [ "$g1_full" -eq 0 ]; then
		echo "G1 全量扫描：${ROOT_DIR}/ 全部可编译"
	else
		echo "⚠️  G1 全量扫描命中（上方 *** Error compiling）。落在本轮变更集之外的命中只告警，"
		echo "    不计入退出码；若下面的严格判定同样命中，才会真阻断。"
	fi
	if [ "${#STRICT_FILES[@]}" -eq 0 ]; then
		echo "─── G1 编译闸 [严格判定] 本轮 ${ROOT_DIR}/ 下无变更的 .py，跳过 ───"
		g1_gate=0
	else
		echo "─── G1 编译闸 [严格判定] 本轮变更的 ${#STRICT_FILES[@]} 个文件 ───"
		python -m compileall -q "${STRICT_FILES[@]}"
		g1_gate=$?
		[ "$g1_gate" -eq 0 ] && echo "G1 通过：本轮变更文件全部可编译"
	fi
fi
echo

# ── 第三步：G2 重复闸 ────────────────────────────────────────────────────────
# python 里重复的 class/def/import 不是语法错误——后者静默覆盖前者，compileall 一律
# exit 0，只能另起 ast 扫描补上。dup-check.py 一趟扫完整棵树，命中按是否落在严格集里
# 分成阻断 / 告警两类，故这里不需要像 G1 那样跑两遍。
echo "─── G2 重复闸 scripts/dup-check.py ───"
if [ "$SUBSET_MODE" -eq 0 ]; then
	python scripts/dup-check.py "$ROOT_DIR"
	g2_gate=$?
else
	STRICT_LIST_FILE="$(mktemp)"
	trap 'rm -f "$STRICT_LIST_FILE"' EXIT
	if [ "${#STRICT_FILES[@]}" -gt 0 ]; then
		printf '%s\n' "${STRICT_FILES[@]}" >"$STRICT_LIST_FILE"
	else
		: >"$STRICT_LIST_FILE"
	fi
	python scripts/dup-check.py --strict-list "$STRICT_LIST_FILE" "$ROOT_DIR"
	g2_gate=$?
fi
echo

# ── 汇总 ────────────────────────────────────────────────────────────────────
if [ "$g1_gate" -ne 0 ] || [ "$g2_gate" -ne 0 ]; then
	echo "ci-syntax 失败：G1=${g1_gate} G2=${g2_gate}"
	exit 1
fi
echo "ci-syntax 通过：G1/G2 在严格判定范围内均无命中"
