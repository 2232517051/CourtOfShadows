## ════════════════════════════════════════════════════════════
## replay.rpy — 二周目成本削减（优化项③）
##
## 1) 章节入口自动存档: 每次真实游玩经过章节开头, 存进隐藏槽位
##    auto_ch-<id>（不占存档页页码）。
## 2) 章节选择"带档开始": 槽位存在时多显示一个按钮, FileLoad 该槽 =
##    属性/人际/前情抉择全部原样带入——不做旗标种子映射, 以后新增
##    旗标也不会漂移。
## 3) 快捷菜单"跳抉择": 快进直达下一个选择点（自定义中文确认框,
##    绕开引擎自带的英文确认文案——本项目未启用翻译框架, _() 对
##    引擎内置串不生效）。
##
## 覆盖规则: 章节选择的白板开局会先置 persistent._skip_next_chapter_autosave,
## 让落地那一次的自动存档跳过——否则白板默认状态会覆盖玩家真周目的槽位。
## 该旗标只对入口有自动存档的章节设置(chapter1-5); 白板局继续往后玩,
## 后续章节照常覆盖(那已经是真实游玩轨迹)。
## ════════════════════════════════════════════════════════════

default persistent._skip_next_chapter_autosave = False

init -5 python:

    def auto_chapter_save(ch_id):
        ## 鉴赏回放里不动存档
        if getattr(renpy.store, "_in_replay", None):
            return
        if persistent._skip_next_chapter_autosave:
            persistent._skip_next_chapter_autosave = False
            return
        try:
            renpy.save("auto_ch-" + ch_id)
        except Exception as exc:
            ## 存档失败（磁盘/回滚边缘）不能打断游戏
            renpy.log("auto_chapter_save({}) failed: {!r}".format(ch_id, exc))

    def SkipToChoice():
        """快进到下一个选择点, 带自定义中文确认框。"""
        return Confirm(
            "即将跳过所有对白，直达下一处抉择。确定？",
            yes=Skip(fast=True, confirm=False),
        )
