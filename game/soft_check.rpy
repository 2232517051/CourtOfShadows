## ============================================================
## 软检定 — soft_check.rpy
## 属性门控从「隐藏选项」改为「可见可选，不足走失败分支」。
## 来源: docs/analysis/KCD2拆解报告 第九章 9.1/9.3(chat 仓库)。
## 试点批次: ch1卷宗 / ch2追问 / ch3暗号 / ch3主教 / ch3突围, 共5处。
##
## 用法(菜单前一行算提示, 选中后第一行落快照):
##   $ _sh = soft_hint("intrigue", 50)
##   menu:
##       "下令调出卷宗[_sh]":
##           if soft_check("ch1_dossier", "intrigue", 50):
##               ... 成功分支(原文)
##           else:
##               ... 失败分支(收益缩水, 文本暗示缺哪条属性)
## ============================================================

## 软检定结果快照。后续章节引用「当时成没成」一律读这里,
## 不要重算——属性会涨落, 重算会让回看文本漂移(铁与誓已踩过这个坑)。
default soft_check_results = {}

## ── 试点批次失败分支 flag(供后续章节做回响/语境修正) ──
default ch1_exp_dossier_stalled = False   ## ch1 卷宗调了读不出方向(chapter1_expansion 软检定试点1)
default ch2_aldric_deflected = False      ## ch2 追问被奥尔德里克岔开, 摄政秘密未泄露(chapter2 试点2)
default ch3_lily_old_code = False         ## ch3 报出的是二十年前的废暗号, 被当成试探者(chapter3 试点3)
default ch3_bishop_grudging = False       ## ch3 对主教的宽恕心口不一, 合作出于亏欠(chapter3 试点4)
default ch3_sortie_costly = False         ## ch3 突围判断对了兵带不动, 折三人无俘获(chapter3 试点5)

init python:
    SOFT_STAT_CN = {
        "power": "权力", "intrigue": "谋略", "faith": "信仰",
        "wealth": "财富", "reputation": "声望", "loyalty": "忠诚",
    }

    def soft_pass(stat_name, threshold):
        """纯判定, 不落快照。只给 soft_hint 等展示用途。"""
        return getattr(store, stat_name, 0) >= threshold

    def soft_check(key, stat_name, threshold):
        """软检定结算: 判定并把结果存进快照, 返回是否通过。
        key 全局唯一(章节_场景 简名)。必须在选中选项后立刻调用,
        让 pass/fail 与玩家做决定那一刻的属性绑定。"""
        result = soft_pass(stat_name, threshold)
        store.soft_check_results[key] = result
        return result

    def soft_hint(stat_name, threshold):
        """菜单选项副行提示。达标返回空串(选项保持干净, 不炫耀);
        不足时返回 |xx不足(需N) 样式后缀, 由 choice screen 的 | 拆分渲染。"""
        if soft_pass(stat_name, threshold):
            return ""
        cn = SOFT_STAT_CN.get(stat_name, stat_name)
        return "|{}不足(需{}) · 强行为之，成败自担".format(cn, threshold)

    def soft_check_cond(key, passed):
        """复合条件版软检定: 通过与否由调用处算好(属性 OR 关系/flag),
        这里只负责落快照并返回。用于像「谋略≥45 或 交情≥50」这类门。"""
        store.soft_check_results[key] = bool(passed)
        return bool(passed)

    def soft_hint_or(stat_name, threshold, alt_ok, alt_label):
        """复合门控(属性 OR 替代条件)的提示版本。
        替代条件成立(alt_ok=True)视同达标; 仅在两头都不足时出提示。
        alt_label 描述替代路径, 例如「或与他交情足够深」。"""
        if alt_ok or soft_pass(stat_name, threshold):
            return ""
        cn = SOFT_STAT_CN.get(stat_name, stat_name)
        return "|{}不足(需{}){} · 强行为之，成败自担".format(cn, threshold, alt_label)
