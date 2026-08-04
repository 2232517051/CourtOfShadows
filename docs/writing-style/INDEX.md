---
schema_version: 1
maturity_stage: seed
---

# 《权谋之庭》原创文风库

## 调用边界

只读取 CANON.md、当前连续上下文与分支事实、guidance.md 中已批准的指导，
以及最多三个活动正例。
正例只能来自用户明确批准的最终文本。没有匹配正例时，标记为
“尚未校准”并进入三稿盲选。
fragment 只能保存用户明确圈定的原句，不得补写衔接。用户撤回正例时，
同步移除样本文件与索引行、重算 maturity_stage，且不转存为反例。
共同特征只有经用户逐条批准并写入 guidance.md 后才能成为活动指导。

## 检索顺序

同角色 > 同 scene_type > 同 text_mode > approved_on 较新。

## 成熟盲测

十二份 full 正例覆盖六类场景各两次后，每轮陌生场景只允许一稿读取
活动正例，另两稿作为不读取正例的对照。三稿使用同一事实卡并随机打乱。
validation-log.md 只按时间顺序记录确认后的轮次元数据，不保存候选原文。

## 活动正例

| ID | scene_type | characters | text_mode | sample_kind | approved_on | sample |
|---|---|---|---|---|---|---|
