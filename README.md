# AI Agent Guardrails

这个仓库用于集中管理面向 AI Agents 的行为约束、编码规范和中英文提示词模板，便于在不同项目场景下复用和持续迭代。

## 仓库用途

- 保存原版参考 guideline。
- 维护我们自己的中英文 `AGENTS` / `CLAUDE` 模板。
- 按主题沉淀可复用规范，例如通用编码规范、Python 自动化项目规范。

## 当前目录结构

```text
ai-agent-guardrails/
├─ AGENTS.md
├─ README.md
├─ Karpathy-Inspired/
│  └─ AGENTS.md
├─ yzk-guideline-cn/
│  ├─ AGENTS_global_cn.md
│  ├─ AGENTS_python_project_cn.md
│  ├─ CLAUDE_global_cn.md
│  └─ CLAUDE_python_project_cn.md
└─ yzk-guideline-en/
   ├─ AGENTS_global_en.md
   ├─ AGENTS_python_project_en.md
   ├─ CLAUDE_global_en.md
   └─ CLAUDE_python_project_en.md
```

## 各目录与文件说明

- `Karpathy-Inspired/`
  - 存放原版参考内容。
  - **不要修改这个目录下面的文件。**

- `AGENTS.md`
  - 仓库级工作规则。
  - 明确了本仓库的维护顺序和同步要求。

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
- 内容侧重于先思考、简单优先、外科手术式改动、先定义成功标准、补充项目级和子目录级 `AGENTS.md` 等原则。

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

## 推荐使用方式

### 新增或修改某个主题

建议按下面顺序操作：

1. 先确认要修改的是哪个主题，例如 `global` 或 `python_project`。
2. 优先编辑 `yzk-guideline-cn/AGENTS_XXX_cn.md`。
3. 再同步更新以下三份同主题文件：
   - `yzk-guideline-cn/CLAUDE_XXX_cn.md`
   - `yzk-guideline-en/AGENTS_XXX_en.md`
   - `yzk-guideline-en/CLAUDE_XXX_en.md`
4. 如果主题范围、命名方式或目录结构发生变化，记得同步更新本 `README.md`。

### 新增一个全新的主题

例如新增 `java_project` 主题时，建议直接创建以下四份文件：

- `yzk-guideline-cn/AGENTS_java_project_cn.md`
- `yzk-guideline-cn/CLAUDE_java_project_cn.md`
- `yzk-guideline-en/AGENTS_java_project_en.md`
- `yzk-guideline-en/CLAUDE_java_project_en.md`

新增后应确保：

- 中英文内容语义一致。
- `AGENTS` 与 `CLAUDE` 内容保持同主题同步。
- 本 `README.md` 的“当前主题划分”部分同步更新。

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
