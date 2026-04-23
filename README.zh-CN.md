# deep-interview

`deep-interview` 是一个 Claude Code skill，用来对用户提供的一组经历材料进行“面试官式”的深度挖掘。

它适用于简历打磨、面试准备、项目经历梳理和能力项提炼等场景。这个 skill 会扫描用户提供的源文件目录，每轮只提出一个高价值问题，指出回答中的薄弱点，记录用户明确接受的增强表述，并在不自动修改原始文件的前提下生成改写预览。

## 这个 skill 能做什么

- 扫描目标目录并找出最值得继续深挖的内容
- 每次只聚焦一个当前目标
- 每轮只问一个有实质价值的问题
- 区分已确认事实、薄弱点和建议表达
- 记录用户接受、可复用的补充内容
- 在长对话中持续维护工作状态
- 生成改写预览，而不是直接覆盖原始内容

## 支持的模式

这个 skill 由六种模式组成：

- `scan`：扫描整个目录，并推荐下一步最适合深挖的目标
- `experience`：围绕单个经历持续深挖，直到它具备面试表达能力
- `theme`：围绕一个能力主题，跨多个经历进行提炼
- `role`：从某个目标岗位视角重新审视材料
- `summarize`：把已有进展压缩成可复用状态
- `finalize`：生成总结和改写预览，但不自动应用到源文件

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── experience-mode.md
    ├── file-handling.md
    ├── finalize-mode.md
    ├── preview-template.md
    ├── role-mode.md
    ├── role-template.md
    ├── scan-mode.md
    ├── session-template.md
    ├── state-template.md
    ├── summarize-mode.md
    ├── theme-mode.md
    └── theme-template.md
```

## 入口文件

主入口文件是：

- `SKILL.md`

它定义了：

- 激活条件
- 核心规则
- 工作目录布局
- 可用模式
- 单轮交互结构
- 回答质量判断规则
- 收尾与预览生成行为

## 使用过程中生成的工作区

当这个 skill 被用于某个用户提供的目录时，它会在该目录下维护一个独立工作区：

```text
deep-interview/
├── state.md
├── sessions/
├── previews/
├── themes/
└── roles/
```

这些文件用于保存面试追问进度和生成的预览内容，默认不会直接改动原始源文件。

## 核心行为约束

这个 skill 会遵守以下关键约束：

- 只在用户明确要求时激活
- 直接读取 Markdown 文件，并单独记录非 Markdown 文件
- 不虚构指标、职责归属或结果
- 深挖过程中始终只保持一个当前目标
- 每轮只提一个问题
- 区分 `Confirmed`、`Suggested` 和 `Accepted` 三类内容
- 只有已确认或已接受的内容才能进入预览
- 不会自动把预览改写回源文件

## 常见触发语句

以下是一些典型的显式触发方式：

- `Use deep-interview on this folder`
- `start scan`
- `start experience: payment platform project`
- `start theme: cross-functional collaboration`
- `start role: backend engineer`
- `summarize current`
- `end interview`

## 适用场景

当用户手里有比较粗糙的项目笔记、简历条目或经历描述，希望通过迭代追问把它们打磨成更强的面试表达材料，而不是直接让模型重写时，这个 skill 会比较合适。

## 说明

- 源文件始终被视为权威记录
- 工作笔记和改写预览会分开保存
- `finalize` 只生成预览，不自动改写原文件
