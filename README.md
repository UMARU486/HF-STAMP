# STPA/HFMEA 医疗流程分析器（MVP）

面向场景：ED triage + handoff（急诊分诊与交接）。

> 仅使用公开/合成案例文本，不使用真实病人隐私数据。

## 目录结构

```text
stpa_tool/
  __init__.py
  cli.py
  schema.py
  extract.py
  analyze.py
  render.py
  utils.py
examples/
  process_ed_triage.md
  case1_delay_ecg.md
  case2_wrong_patient_id.md
  case3_handoff_missing_allergy.md
tests/
  test_extract.py
  test_cli_smoke.py
README.md
pyproject.toml
.gitignore
```

## 安装

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## CLI 帮助

```bash
python -m stpa_tool --help
```

## 运行分析

```bash
python -m stpa_tool analyze examples/case1_delay_ecg.md --out outputs/
```

当前初始版本可运行并导出以下文件（即使内容为空）：

- hazards.csv
- stpa_uca.csv
- constraints.csv
- summary.md

## 测试

```bash
pytest -q
```

## 说明

- 当前为骨架版本，`extract.py` 为占位实现（返回空列表）。
- 后续可逐步补充规则或提示词模板，实现半自动抽取与风险分析。
