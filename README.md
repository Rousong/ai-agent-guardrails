# AI Agent Guardrails

这个仓库用于集中管理面向 AI Agents 的行为约束、编码规范和中英文提示词模板，便于在不同项目场景下复用和持续迭代。

## 仓库用途

- 保存原版参考 guideline。
- 维护我们自己的中英文 `AGENTS` / `CLAUDE` 模板。
- 按主题沉淀可复用规范，例如通用编码规范、Python 自动化项目规范。
- 用本地校验脚本确认同主题的四份模板没有缺失或漏同步。

## 当前目录结构

```text
ai-agent-guardrails/ # AI Agent guideline 模板仓库。
├─ .gitignore # 仓库级忽略规则，避免提交本地系统文件。
├─ AGENTS.md # 仓库级工作规则和目录说明。
├─ README.md # 仓库用途、主题划分、使用方式和维护流程说明。
├─ Karpathy-Inspired/ # 原版参考内容目录，不要修改这里的文件。
│  └─ AGENTS.md # Karpathy 原版风格的 AGENTS 参考规则。
├─ scripts/ # 仓库维护脚本目录。
│  ├─ AGENTS.md # scripts 目录自己的维护说明。
│  └─ validate_guidelines.py # 只读校验脚本，检查 guideline 四文件矩阵和 README 索引。
├─ yzk-guideline-cn/ # 我们维护的中文版 guideline 模板目录。
│  ├─ AGENTS_global_cn.md # 中文 AGENTS 通用行为准则模板。
│  ├─ AGENTS_python_project_cn.md # 中文 AGENTS Python 自动化项目规范模板。
│  ├─ CLAUDE_global_cn.md # 中文 CLAUDE 通用行为准则模板。
│  └─ CLAUDE_python_project_cn.md # 中文 CLAUDE Python 自动化项目规范模板。
└─ yzk-guideline-en/ # 我们维护的英文版 guideline 模板目录。
   ├─ AGENTS_global_en.md # 英文 AGENTS 通用行为准则模板。
   ├─ AGENTS_python_project_en.md # 英文 AGENTS Python 自动化项目规范模板。
   ├─ CLAUDE_global_en.md # 英文 CLAUDE 通用行为准则模板。
   └─ CLAUDE_python_project_en.md # 英文 CLAUDE Python 自动化项目规范模板。
```

## 各目录与文件说明

- `Karpathy-Inspired/`
  - 存放原版参考内容。
  - **不要修改这个目录下面的文件。**

- `AGENTS.md`
  - 仓库级工作规则。
  - 明确了本仓库的维护顺序和同步要求。

- `scripts/`
  - 存放仓库维护脚本。
  - 当前包含只读 guideline 校验脚本。

- `yzk-guideline-cn/`
  - 我们维护的中文版 guideline。
  - 修改时优先从这里的 `AGENTS_XXX_cn.md` 开始。

- `yzk-guideline-en/`
  - 与中文版对应的英文版 guideline。
  - 必须与中文版本保持主题和语义同步。

## 当前主题划分

### 1. `global`

文件：
- `yzk-guideline-cn/AGENTS_global_cn.md`
- `yzk-guideline-cn/CLAUDE_global_cn.md`
- `yzk-guideline-en/AGENTS_global_en.md`
- `yzk-guideline-en/CLAUDE_global_en.md`

用途：
- 存放通用型的 AI 编码行为约束。
- 适合在大多数项目中作为基础规则使用。
- 内容侧重于先思考、简单优先、外科手术式改动、先定义成功标准、补充项目级和子目录级对应文档等原则。

### 2. `python_project`

文件：
- `yzk-guideline-cn/AGENTS_python_project_cn.md`
- `yzk-guideline-cn/CLAUDE_python_project_cn.md`
- `yzk-guideline-en/AGENTS_python_project_en.md`
- `yzk-guideline-en/CLAUDE_python_project_en.md`

用途：
- 存放 Python 自动化项目专用规范。
- 适合叠加在 `global` 规则之上使用。
- 当前内容包括：
  - 始终使用当前目录的 `.venv`
  - 安装、删除、调整依赖后同步维护 `requirements.txt`
  - Python 模块头模板
  - 方法外部标题注释模板
  - 函数 / 方法 `docstring` 书写要求
  - 参数类型和返回值类型必须显式声明
  - 供 Agent 追加项目概述和结构树的明确动态区块

## 如何应用到真实项目

1. 先根据目标工具选择文档类型：
   - Codex / 通用 Agent 项目使用 `AGENTS_<topic>_<lang>.md`。
   - Claude 项目使用 `CLAUDE_<topic>_<lang>.md`。
2. 再根据目标项目语言选择中英文版本：
   - 中文项目优先使用 `_cn`。
   - 英文项目优先使用 `_en`。
3. 先复制或合并 `global` 主题，再按项目类型叠加专用主题，例如 Python 自动化项目再合并 `python_project`。
4. 如果目标项目已经有自己的项目规则，不要直接覆盖；把本仓库模板与项目特定规则合并，保留更具体的项目要求。
5. 合并后检查文档类型措辞是否正确：`AGENTS` 文件只写 `AGENTS.md`，`CLAUDE` 文件只写 `CLAUDE.md`。

## 维护规则

本仓库遵循以下固定流程：

1. 不要修改 `Karpathy-Inspired` 目录下面的内容。
2. 当需要修改某个主题时，优先修改 `yzk-guideline-cn` 下对应的 `AGENTS_XXX_cn.md`。
3. 只要新增或修改了某个 `AGENTS` 主题，就必须同步处理以下三份对应文件：
   - `yzk-guideline-en` 下对应的 `AGENTS_XXX_en.md`
   - `yzk-guideline-cn` 下对应的 `CLAUDE_XXX_cn.md`
   - `yzk-guideline-en` 下对应的 `CLAUDE_XXX_en.md`
4. 也就是说，同名主题必须始终保持这四份文件一起同步：
   - 中文 `AGENTS`
   - 英文 `AGENTS`
   - 中文 `CLAUDE`
   - 英文 `CLAUDE`
5. 如果主题范围、命名方式或目录结构发生变化，同步更新本 `README.md` 和根目录 `AGENTS.md`。

## 验证同步状态

修改 guideline 后运行：

```bash
python3 scripts/validate_guidelines.py
```

这个脚本会只读检查：
- 每个主题是否同时存在中文 `AGENTS`、英文 `AGENTS`、中文 `CLAUDE`、英文 `CLAUDE` 四份文件。
- `README.md` 是否列出了每个主题和对应的四份文件。
- guideline 模板内部是否出现 `AGENTS.md or CLAUDE.md` 这类混写措辞。
- `AGENTS` 模板是否误写 `CLAUDE.md`，以及 `CLAUDE` 模板是否误写 `AGENTS.md`。

如果需要在临时目录中验证复制出来的仓库，可以使用：

```bash
python3 scripts/validate_guidelines.py --root /path/to/copied/repo
```

## 新增或修改某个主题

建议按下面顺序操作：

1. 先确认要修改的是哪个主题，例如 `global` 或 `python_project`。
2. 优先编辑 `yzk-guideline-cn/AGENTS_XXX_cn.md`。
3. 再同步更新以下三份同主题文件：
   - `yzk-guideline-cn/CLAUDE_XXX_cn.md`
   - `yzk-guideline-en/AGENTS_XXX_en.md`
   - `yzk-guideline-en/CLAUDE_XXX_en.md`
4. 更新 `README.md` 和根目录 `AGENTS.md` 中的主题说明、目录结构或维护规则。
5. 运行 `python3 scripts/validate_guidelines.py` 验证同步状态。

## 新增一个全新的主题

例如新增 `java_project` 主题时，建议直接创建以下四份文件：

- `yzk-guideline-cn/AGENTS_java_project_cn.md`
- `yzk-guideline-cn/CLAUDE_java_project_cn.md`
- `yzk-guideline-en/AGENTS_java_project_en.md`
- `yzk-guideline-en/CLAUDE_java_project_en.md`

新增后应确保：

- 中英文内容语义一致。
- `AGENTS` 与 `CLAUDE` 内容保持同主题同步。
- 本 `README.md` 的“当前主题划分”部分同步更新。
- 根目录 `AGENTS.md` 的目录结构树同步更新。
- `python3 scripts/validate_guidelines.py` 可以通过。

## 命名约定

- 中文 `AGENTS`：`AGENTS_<topic>_cn.md`
- 英文 `AGENTS`：`AGENTS_<topic>_en.md`
- 中文 `CLAUDE`：`CLAUDE_<topic>_cn.md`
- 英文 `CLAUDE`：`CLAUDE_<topic>_en.md`

其中：
- `<topic>` 表示主题，例如 `global`、`python_project`
- `_cn` 表示中文版本
- `_en` 表示英文版本

## 说明

- 这个仓库当前已经不再使用旧的 `ori`、`python` 命名方式，现以 `global`、`python_project` 为准。
- 如果后续继续拆分更多项目场景，建议沿用当前的主题化命名方式，保持目录结构稳定、可预测。
