# PAPER 使用命令指南

本指南收集可直接复制到 Codex / Agent 对话中的常用命令。推荐所有论文任务都以“使用 PAPER”开头。

## 1. 完整论文任务

```text
使用 PAPER。我要写一篇[论文类型]，方向是[学科/主题]，目标是[期刊/会议/学校]。
我提供的材料包括：[材料列表]。
请先确认论文类型、模板要求、输出格式和缺失信息，再规划完整写作流程。
```

## 2. 确认论文类型和模板

```text
使用 PAPER，帮我确认这篇论文的写作类型、目标期刊/会议/学校格式、篇幅、图表公式和参考文献要求。
模板或投稿指南如下：[粘贴规则或提供文件]。
```

## 3. 根据材料规划目录

```text
使用 PAPER，根据我提供的论文、实验数据和草稿，规划一篇[论文类型]的目录。
请说明每一章/节使用哪些材料，列出缺失内容、术语表和潜在重复风险。
```

## 4. 写作、润色、翻译

```text
使用 PAPER，把下面这段内容改写为[中文/英文/Nature 风格/SCI 风格]。
要求：保留技术含义和数值，不添加新结果，不虚构引用，指出逻辑缺口。
文本如下：
[粘贴文本]
```

## 5. 快速小任务

```text
使用 PAPER，fast_track=true。请只润色下面这一段，不改变技术含义，并给出残余风险。
[粘贴一小段文本]
```

## 6. 引用检查

```text
使用 PAPER，逐句检查下面段落的引用需求。
请拆分 claim，判断是否需要引用，给出候选文献支持等级，并指出缺失证据。
[粘贴段落和可用文献]
```

## 7. 生成论文图

```text
使用 PAPER，根据以下实验数据生成论文图。
请先给出 figure contract，再生成图件。输出 SVG 和 PNG，并检查坐标轴、单位、图例、统计标注、caption 和正文 claim 是否一致。
[粘贴数据或说明数据文件]
```

## 8. Word / LaTeX / Markdown 排版

```text
使用 PAPER，按照这个[Word/LaTeX/Markdown]模板排版我的论文。
请检查标题层级、图表、公式、参考文献、页眉页脚和模板合规性。
不要改变技术含义。
```

## 9. 投稿或答辩前终审

```text
使用 PAPER，对这篇[SCI/会议/中文期刊/硕士论文]做提交前终审。
重点检查语言、逻辑、引用、图文一致性、模板合规性和审稿人可能质疑的问题。
```

## 10. 审稿意见回复

```text
使用 PAPER，根据以下审稿意见和我的修改稿，生成 point-by-point response letter。
请区分已经修改、需要补充、不能完全满足和需要解释的意见，并生成修改记录。
[粘贴审稿意见和修改说明]
```

## 11. 论文转 PPTX

```text
使用 PAPER，把这篇论文做成[页数]页[中文/英文/双语] PPTX，用于[组会/答辩/课程汇报/论文分享]。
请提取论文主线，选择关键图表，写 slide title、要点、caption 和 speaker notes，并生成 QA 报告。
```

PPTX 依赖检查：

```powershell
python C:\Users\Compus\.agents\skills\PAPER\scripts\check_ppt_dependencies.py
```

## 12. 推荐模块路线

| 任务 | 推荐路线 |
|---|---|
| 从零写论文 | `paper_type -> paper_plan -> paper_content -> paper_document -> paper_final` |
| 只润色草稿 | `paper_content -> paper_final` |
| 只排版文档 | `paper_document -> paper_final` |
| 审稿修回 | `paper_revision -> paper_content -> paper_document -> paper_final` |
| 论文转 PPT | `paper_ppt` |
| 质量较差需重建 | `paper_workflow_controller -> paper_plan -> paper_content` |
