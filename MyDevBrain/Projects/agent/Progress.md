
## 相关笔记

- [[Projects/agent/README]] - Agent 项目概述
- [[Projects/agent/Decisions]] - 架构决策记录
- [[Daily/2026-05-23]] - 早期进展记录
- [[Daily/2026-05-25]] - 最新进度更新
# Progress - 项目进度追踪

## 当前进度

**更新时间**: 2026-05-23

## 本周重点

- [x] 分析现有 osa 代码库
- [ ] 确定技术选型

## 待办事项

- [ ] 设计 Agent 架构
- [ ] 实现基础对话功能
- [ ] 集成 MCP 工具

## 已完成

- [x] 项目初始化
- [x] 代码位置确认：~/code/osa
- [x] 会议纪要整理
- [x] 安装 Poppler (PDF 工具)

### Code-Snippets 目录

用于存放项目中常用的代码片段：

- **功能模块**：可复用的 Python 函数、LangChain 工具
- **Prompt 模板**：系统提示词、用户提示词
- **配置示例**：API 配置、环境变量模板
- **调用示例**：MiniMax/Claude API 调用代码

### 会议纪要

- `meeting/ADR研究总结-健康管家AI Agent战略对齐会.pdf`
- `meeting/健康管家MVP战略对齐会ADR.pdf`

### PDF 要点提取

**ADR研究总结会 (2026-05-21):**
- MVP 目标：12周 32+1 阿尔文 Agent demo
- 技术路线：GraphRAG + Agent + App
- 模型对比：Alvin skill 3.9MB vs App 787KB

**MVP战略对齐会 (2026-05-20):**
- MVP 定义：Apple Watch + Agent = 80%自研 + 10% OPPO
- 数据源：Apple Watch HRV、睡眠、血氧
- 模型：MiniMax 2.5/2.7、DeepSeek V4 Pro、Claude Opus 4.7

### 会议纪要

- `meeting/ADR研究总结-健康管家AI Agent战略对齐会.pdf` - ADR 研究总结
- `meeting/健康管家MVP战略对齐会ADR.pdf` - MVP 战略对齐会

---

## osa 代码库分析

### 项目概述
OSA (Obstructive Sleep Apnea) 睡眠呼吸暂停健康分析 Agent

### 3种运行模式

| 文件 | 方式 | LLM | 说明 |
|------|------|-----|------|
| `sleep_apnea_interactive.py` | 关键字匹配 | 无 | 离线快速响应 |
| `gradio_app.py` | ReAct Agent | MiniMax | Gradio Web UI |
| `sleep_apnea_langchain_minimax.py` | ReAct Agent | MiniMax | 完整对话记忆 |

### 核心架构

```
数据源(latest-health-data.json) ──► @tool函数 ──► Agent ──► 用户输出
                          │
                    LLM(MiniMax) ──┘
```

### @tool 函数 (4个)

1. `get_blood_oxygen()` - 血氧饱和度
2. `get_hrv_analysis()` - 心率变异性
3. `get_sleep_quality()` - 睡眠阶段
4. `get_activity_risk()` - 活动量

### 数据源格式

- `latest-health-data.json` - Apple Health 30天数据
- 指标：oxygenSaturation, heartRateVariabilitySDNN, sleepAnalysis, stepCount

### 技术栈

- LLM: MiniMax-M2.7
- 框架: LangChain, Gradio
- 数据: JSON (Apple Health 导出)

---

## 阻塞问题

- 无