.PHONY: clean-pyc clean-build docs clean

# Browser Tools
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# UCloud Tools Path
UCLOUD_TEMPLATE_PATH=../ucloud-api-model-v2/apisdk/lang/python/templates

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

# unit test
test: clean
	pytest

# --cov-report 两项显式写全：只要指定了 --cov-report，pytest-cov 就不再自动出 term 报告。
# xml 是给 codecov-action 用的——它只上传现成的报告文件，不会自己去生成
# （Travis 时代那个 codecov bash uploader 会顺手跑 `coverage xml`，action 不会）。
test-cov: clean
	pytest --cov=ucloud/core tests --cov-report=term --cov-report=xml

test-cov-html:
	pytest --cov=ucloud/core tests --cov-report html
	$(BROWSER) htmlcov/index.html

test-acc: clean
	USDKACC=1 pytest --cov=ucloud

test-all: clean
	tox

# CI 门禁：生成代码必须能被解释器接受、且无重复声明。门禁只管「代码能不能用」，
# 不管风格——语法错误、非法标识符、重复声明是缺陷，缩进和空行不是。
#   G1 `compileall` 覆盖 ucloud/ 下全部生成代码（现有 lint 显式 --exclude 掉了
#      ucloud/services，也就是生成代码一直没人查）。真缺陷它抓得住，实测：
#      `def uai-modelverse(self):`（连字符产品名回填成非法标识符，真实事故形态）
#      → exit 1 SyntaxError；而纯格式问题 `def  foo( a,b ):` → exit 0。
#      这正是想要的分界线。
#   G2 python 里重复的 class/def/import 不是语法错误——后者静默覆盖前者，
#      compileall 一律 exit 0，只能另起 ast 扫描补上。
#      真实案例：uphost 的 get_phost_disk_upgrade_price 被生成了两遍，
#      后者是已删除 API 的旧快照，把唯一在用的那个覆盖掉了。
#
# 两条闸都**全量扫描、只对本轮变更的文件阻断**，实现收进 scripts/ci-syntax.sh：
# G2 那个真实案例就躺在上游 master 上，整棵树一律阻断的话，发**任何一个**产品
# （UDisk、UNet……）的 codegen PR 都会被这处与本次发布毫无关系的存量问题判红，
# mergeable_state 变 unstable，自动合并永久失效——那正是这套门禁要解决的问题本身。
# 同源决策见 ucloud-sdk-release/scripts/python-fatal-check.sh（2026-07-31，已被
# pipeline 2507836 实证）。变更集怎么算、拿不到时怎么 fail-closed 退回整棵树，
# 见 scripts/ci-syntax.sh 文件头。本地不设 CI_BASE_SHA，看到的就是整棵树严格判定。
#
# 这里**故意不放** `black --check`，与 go 的 ci-syntax 带 gofmtcheck.sh 不对称，
# 不是漏了：
#   · gofmt 的输出多年稳定，版本又由 workflow 里的 setup-go 钉住，两端天然对齐；
#     black 每年改一次稳定风格——实测本仓 392 个文件在 24.8.0 / 24.10.0 下全过，
#     到 25.1.0 起有 211 个被判需重排（改了 docstring 首尾空白的处理）。
#   · 而生成侧 ucloud-sdk-release 的 python:format job 是 `pip install -U black`
#     之后跑 `make fmt`，永远用当天最新版格式化并提交。校验端无论钉哪个版本，
#     都会在 black 发新版后与生成侧偏斜，把每个 codegen PR 恒判为红——
#     那恰好是自动合并要解决的问题本身。
#   · 格式化是生成侧 `make fmt` 的职责，生成时已经跑过，门禁再 --check 一遍
#     不增加保障，只增加版本偏斜的风险。
.PHONY: ci-syntax
ci-syntax:
	@bash scripts/ci-syntax.sh

lint:
	@flake8 --exclude=ucloud/services ucloud --ignore=E501,F401

fmt:
	@black -l 80 ucloud tests examples

dev:
	@pip install -e .[dev]

docs:
	#sphinx-apidoc -o docs/services ucloud/services
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

docs-preview:
	$(BROWSER) docs/_build/html/index.html

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

version:
	@python -c 'from ucloud.version import version; print(version)'

codegen:
	@bash ./scripts/codegen.sh

release-check:
	@python scripts/release.py --dry-run

release:
	@python scripts/release.py
