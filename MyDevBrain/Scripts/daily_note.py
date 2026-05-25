#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日工作日记自动生成脚本
每天自动记录当日进度和工作情况，并给出改进建议
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path

# ==================== 配置 ====================
VAULT_PATH = Path(r"C:\Users\zdeer\Documents\Obsidian Vault\MyDevBrain")
PROGRESS_FILE = VAULT_PATH / "Projects/agent/Progress.md"
DAILY_DIR = VAULT_PATH / "Daily"
TEMPLATE_FILE = TEMPLATE_DIR = VAULT_PATH / "Templates/daily_template.md"

# ==================== 读取进度文件 ====================
def read_progress():
    """读取 Progress.md 中的待办和已完成项"""
    if not PROGRESS_FILE.exists():
        return {"待办": [], "已完成": [], "本周重点": []}

    content = PROGRESS_FILE.read_text(encoding="utf-8")

    待办 = []
    已完成 = []

    # 解析待办事项
    in_todo = False
    in_done = False
    for line in content.split("\n"):
        if "## 待办事项" in line:
            in_todo = True
            in_done = False
        elif "## 已完成" in line:
            in_todo = False
            in_done = True
        elif "## 本周重点" in line:
            break
        elif "- [ ]" in line and in_todo:
            待办.append(line.replace("- [ ] ", "").strip())
        elif "- [x]" in line and in_done:
            已完成.append(line.replace("- [x] ", "").strip())

    return {"待办": 待办, "已完成": 已完成}

# ==================== 生成改进建议 ====================
def generate_advice(progress_data):
    """根据进度数据生成改进建议"""
    todo_count = len(progress_data["待办"])
    done_count = len(progress_data["已完成"])

    advice = []

    if done_count == 0:
        advice.append("⚠️ 今日暂无完成项，建议优先完成一件小事建立成就感")

    if todo_count > 5:
        advice.append("📋 待办较多，建议拆分成更小的任务")

    # 基于项目阶段建议
    advice.append("💡 建议：每天优先处理一个阻碍进度的阻塞问题")

    return "\n".join(advice) if advice else "✅ 今日状态良好，继续保持！"

# ==================== 生成工作日记 ====================
def generate_daily_note():
    """生成当日的日记文件"""
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][today.weekday()]

    # 读取进度数据
    progress = read_progress()

    # 构建日记内容
    daily_note = f"""# 工作日记 - {date_str} {weekday}

## 今日进度

### 已完成
{chr(10).join(f"- [x] {item}" for item in progress["已完成"]) if progress["已完成"] else "- (无)"}

### 待办
{chr(10).join(f"- [ ] {item}" for item in progress["待办"]) if progress["待办"] else "- (无)"}

---

## 改进建议

{generate_advice(progress)}

---

*Auto-generated at {today.strftime("%Y-%m-%d %H:%M:%S")}*
"""

    # 确保 Daily 目录存在
    DAILY_DIR.mkdir(exist_ok=True)

    # 写入日记文件
    output_file = DAILY_DIR / f"{date_str}.md"
    output_file.write_text(daily_note, encoding="utf-8")

    print(f"[OK] Generated: {output_file}")
    return output_file

if __name__ == "__main__":
    print("[Daily Note] Generating...")
    generate_daily_note()