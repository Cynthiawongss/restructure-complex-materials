# 安装与使用 / Installation

[中文首页](../README.md) · [English](../README.en.md)

## 最简单：让 Codex 安装

在具备 skill-installer 的 Codex 环境中发送：

~~~text
请使用 skill-installer 安装：
https://github.com/cynthiawongss/restructure-complex-materials/tree/main/skills/restructure-complex-materials
~~~

这是明确的技能目录，里面有 SKILL.md。收藏仓库或下载整个源码包不会自动完成安装。若当前环境没有安装器，使用下面的手动方式。

新安装的技能应可在后续交互中发现；如果没有出现，检查安装位置与启用状态，再重启客户端。不同客户端版本可能有所不同，参见 [官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

## 手动安装

1. 在 [v0.1.0 发布页](https://github.com/cynthiawongss/restructure-complex-materials/releases/tag/v0.1.0) 下载 `restructure-complex-materials-v0.1.0.zip`（英文指令）或 `restructure-complex-materials-v0.1.0-zh-CN.zip`（中文指令）。
2. 解压得到 `restructure-complex-materials/` 文件夹，里面直接包含 SKILL.md 与 agents/openai.yaml。
3. 将这个文件夹放到当前项目的 `.agents/skills/` 下；支持该用户级目录的 Codex 版本也可以放到 `~/.agents/skills/`。
4. 若已有同名技能，先保留旧版，再用一个版本替换；不要并排安装中英文两个同名版本。

手动项目安装后的结构：

~~~text
your-project/
└── .agents/
    └── skills/
        └── restructure-complex-materials/
            ├── SKILL.md
            ├── LICENSE
            └── agents/
                └── openai.yaml
~~~

自动安装器可能按其客户端版本选择不同的用户级目录，请以安装器报告的位置为准。安装目标是技能子目录，不是整个仓库。

也可下载 GitHub 源码 ZIP，从 `skills/restructure-complex-materials/` 取出技能文件夹。中文替代指令位于 [docs/SKILL.zh-CN.md](SKILL.zh-CN.md)；要用中文运行指令，将其复制为同一安装目录的 SKILL.md，替换英文入口即可。

## 不记得名字时

安装并启用后，先直接描述你要做的事。描述匹配时，Codex 可以选用技能；不保证每次匹配。要明确指定，可以发送：

~~~text
使用 $restructure-complex-materials，处理我接下来提供的任务和资料。
~~~

自然语言匹配和选择器操作会随客户端变化；官方文档区分显式与隐式调用。SKILL.md 的语言不限制用户使用中文或英文发起任务。

## 更新与移除

记录安装器给出的实际目录。更新前保留本地定制，再替换该目录中的技能文件。移除时只移除这个技能目录，不需要改动项目资料。两个语言 ZIP 使用相同技能名称，属于替代版本。

## English quick guide

Ask Codex's skill-installer to install the GitHub directory above. Alternatively, download one language-specific release ZIP and place the extracted `restructure-complex-materials` folder in your project's `.agents/skills/` directory. Current documented Codex versions also support `~/.agents/skills/` for user-level discovery. Installer-managed locations may differ by client version.

Install only one language variant. The repository has one runnable entry point in `skills/restructure-complex-materials/SKILL.md`; the Chinese document is an alternative file, not a second installed skill. Release ZIPs contain the ready-to-copy skill folder and license.

Describe your task naturally, or invoke `$restructure-complex-materials` explicitly. If the skill is missing, check the path and enabled state, then restart the client if needed. Keep local customizations before replacing an installed version.

Reference: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills).
