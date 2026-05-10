# AGENTS.md

## 项目用途

如果修改此项目里面的代码文件或维护脚本，那么请同步更新此 MD 文档。

本仓库用于集中维护面向 AI Agents 的行为约束、编码规范和中英文提示词模板。仓库内同时保存原版参考内容，以及我们自己的 `AGENTS` / `CLAUDE` 中英文主题模板。

## 目录结构

```text
HarnessProject/ # AI Agent guideline 模板仓库，维护中英文 AGENTS / CLAUDE 规则。
├─ .gitignore # 仓库级忽略规则，避免提交本地系统文件。
├─ AGENTS.md # 仓库级工作规则和目录说明。
├─ README.md # 面向使用者的仓库用途、主题划分和维护流程说明。
├─ Karpathy-Inspired/ # 原版参考内容目录，不要修改这里的文件。
│  └─ AGENTS.md # Karpathy 原版风格的 AGENTS 参考规则。
├─ scripts/ # 仓库维护脚本目录。
│  ├─ AGENTS.md # scripts 目录自己的维护说明。
│  └─ validate_guidelines.py # 只读校验脚本，检查 guideline 四文件矩阵和 README 索引。
├─ yzk-guideline-cn/ # 我们维护的中文版 guideline 模板目录。
│  ├─ AGENTS_global_cn.md # 中文 AGENTS 通用行为准则模板。
│  ├─ AGENTS_python_project_cn.md # 中文 AGENTS Python 自动化项目规范模板。
│  ├─ AGENTS_python_project_uv_cn.md # 中文 AGENTS Python 项目 uv 管理规范模板。
│  ├─ CLAUDE_global_cn.md # 中文 CLAUDE 通用行为准则模板。
│  ├─ CLAUDE_python_project_cn.md # 中文 CLAUDE Python 自动化项目规范模板。
│  └─ CLAUDE_python_project_uv_cn.md # 中文 CLAUDE Python 项目 uv 管理规范模板。
└─ yzk-guideline-en/ # 我们维护的英文版 guideline 模板目录。
   ├─ AGENTS_global_en.md # 英文 AGENTS 通用行为准则模板。
   ├─ AGENTS_python_project_en.md # 英文 AGENTS Python 自动化项目规范模板。
   ├─ AGENTS_python_project_uv_en.md # 英文 AGENTS Python project uv workflow template.
   ├─ CLAUDE_global_en.md # 英文 CLAUDE 通用行为准则模板。
   ├─ CLAUDE_python_project_en.md # 英文 CLAUDE Python 自动化项目规范模板。
   └─ CLAUDE_python_project_uv_en.md # 英文 CLAUDE Python project uv workflow template.
```

## 固定维护规则

1. 不要修改 `Karpathy-Inspired/` 目录下面的内容，这是原版参考内容。
2. 修改既有主题时，先修改 `yzk-guideline-cn/AGENTS_<topic>_cn.md`。
3. 修改或创建 `AGENTS_<topic>_cn.md` 后，必须同步处理同主题的另外三份文件：
   - `yzk-guideline-en/AGENTS_<topic>_en.md`
   - `yzk-guideline-cn/CLAUDE_<topic>_cn.md`
   - `yzk-guideline-en/CLAUDE_<topic>_en.md`
4. 同名主题必须始终保持四份文件一起同步：中文 `AGENTS`、英文 `AGENTS`、中文 `CLAUDE`、英文 `CLAUDE`。
5. 如果新增、删除或重命名主题，同步更新 `README.md` 的主题列表、目录结构和维护说明。
6. 修改完成后运行 `python3 scripts/validate_guidelines.py`，确认四文件矩阵和 README 索引仍然一致。

## 子目录文档规则

创建新的子目录时，先在该目录内创建自己的 `AGENTS.md`。如果修改某个子目录中的代码文件，也要同步更新该目录的 `AGENTS.md`。

`yzk-guideline-cn/` 和 `yzk-guideline-en/` 是模板集合目录，不为每个模板文件额外创建子目录级 `AGENTS.md`。
