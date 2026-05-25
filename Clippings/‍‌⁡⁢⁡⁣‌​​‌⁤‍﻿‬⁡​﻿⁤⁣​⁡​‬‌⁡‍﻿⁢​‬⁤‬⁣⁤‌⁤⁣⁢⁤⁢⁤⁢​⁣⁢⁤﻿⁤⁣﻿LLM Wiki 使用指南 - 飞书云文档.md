---
title: "‍‌⁡⁢⁡⁣‌​​‌⁤‍﻿‬⁡​﻿⁤⁣​⁡​‬‌⁡‍﻿⁢​‬⁤‬⁣⁤‌⁤⁣⁢⁤⁢⁤⁢​⁣⁢⁤﻿⁤⁣﻿LLM Wiki 使用指南 - 飞书云文档"
source: "https://mcnv53qu24c6.feishu.cn/wiki/VG81wFQFZitH8Ikr7UdcUNJXnzb"
author:
published:
created: 2026-05-25
description:
tags:
  - "clippings"
---
## 飞书云文档

搜索

输入“/”快速插入内容

llm-wiki/

├── CLAUDE.md ← 核心 schema，告诉 AI 如何维护 wiki

├── raw/ ← 原始文档（文章/PDF/图片），不可修改

├── wiki/ ← AI 生成的 markdown 文件

│ ├── index.md ← 内容目录，所有页面的索引

│ ├── log.md ← 追加式操作日志

│ ├── sources/ ← 源文档摘要页

│ ├── entities/ ← 实体页（人物/项目/产品）

│ ├── concepts/ ← 概念页（技术/理论/模式）

│ └── synthesis/ ← 综合分析页

└── assets/ ← 图片附件

💡

关键原则：raw/ 下的文件永不修改，只有 wiki/ 下的页面由 AI 读写。

三、三个核心操作

1\. Ingest（摄入）

把文档扔进 raw/，告诉 AI："帮我 ingest 这篇"

AI 自动完成：

•

读文档 → 写摘要页到 wiki/sources/

•

更新 index.md

•

更新相关概念/实体页（可能涉及 10-15 个页面）

•

追加 log.md 记录

2\. Query（查询）

直接向 AI 提问。好的回答会自动沉淀为 wiki 新页面，让探索可复合。

3\. Lint（体检）

告诉 AI 要"lint 一下 wiki"，检查：

•

页面间矛盾

•

被新文献过时的旧结论

•

孤儿页面（无 inbound 链接）

•

提及但未建页的概念

•

缺失的交叉引用

四、页面规范

Frontmatter 格式

YAML frontmatter

\---

title: 页面标题

tags: \[tag1, tag2\]

created: 2026-05-25

updated: 2026-05-25

sources: \[source-refs\]

\---

\## Summary

2-3 句概述

\## Details

正文内容

\## See Also

\- \[\[相关页面\]\]

•

qmd：本地 BM25/vector 搜索，MCP 服务器

评论（0）

跳转至首条评论

真诚点赞，手留余香

0 字

- 上传日志

- 联系客服

- 功能更新

- 帮助中心

- 效率指南