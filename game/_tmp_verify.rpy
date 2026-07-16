## 临时验证 — 全流程: 第一章 → 外章 → 第二章 → … → 第五章。验完即删。
## COS_GATE=go|delegate 控制在可选门选哪条。
## 注意: chapter1_start 末尾是 jump chapter2_start(不返回), 所以用周期性快照记录状态,
## 跑到哪记到哪 —— 不能靠 call 之后的 label。
init 999 python:
    import os, io
    _GATE = os.environ.get("COS_GATE", "go")
    _OUT = os.path.join(os.environ.get("TEMP", "."), "full_%s.txt" % _GATE)
    config.label_overrides["splashscreen"] = "_tmp_verify_entry"

    _TRACE = []
    _REL = []
    _o = _apply_rel_effects_python
    def _c(*a, **kw):
        _REL.append(1)
        _TRACE.append("  · apply_rel_chapter_effects 第 %d 次" % len(_REL))
        return _o(*a, **kw)
    store._apply_rel_effects_python = _c

    def _menu(items):
        vis = [(l, v) for l, v in items if v is not None and getattr(v, "sensitive", True) is not False]
        if not vis: return None
        if any("中间商" in l for l, v in vis):
            want = "中间商" if _GATE == "delegate" else "亲自去"
            for l, v in vis:
                if want in l:
                    _TRACE.append("[可选门] → " + l[:26])
                    return getattr(v, "value", v)
        return getattr(vis[0][1], "value", vis[0][1])
    store.menu = _menu

    renpy.call_screen = lambda _n, *a, **kw: None

    _N = [0]
    def _spy(who, what, *a, **kw):
        _N[0] += 1
        return None
    renpy.say = _spy

    ## 章节卡是最可靠的进度标记
    _real_show_chapter = None
    _seen_ch = []

    def _snapshot():
        try:
            lines = list(_TRACE)
            lines.append("")
            lines.append("--- 快照 ---")
            lines.append("对话行数: %d" % _N[0])
            lines.append("当前 label: %r" % (renpy.get_filename_line(),))
            lines.append("southern_outcome = %r" % getattr(store, "southern_outcome", "?"))
            lines.append("apply_rel_chapter_effects 累计 = %d  (主线 ch2-5 应为 4)" % len(_REL))
            lines.append("属性: power=%s intrigue=%s faith=%s loyalty=%s reputation=%s wealth=%s" % (
                getattr(store,'power','?'), getattr(store,'intrigue','?'), getattr(store,'faith','?'),
                getattr(store,'loyalty','?'), getattr(store,'reputation','?'), getattr(store,'wealth','?')))
            lines.append("已完成章节: %r" % (sorted(persistent.chapters_completed or []),))
            lines.append("ending_type = %r" % getattr(store, "ending_type", "<未设>"))
            io.open(_OUT, "w", encoding="utf-8").write("\n".join(lines))
        except Exception as e:
            pass

    _tick = [0]
    def _periodic():
        _tick[0] += 1
        if _tick[0] % 60 == 0:
            _snapshot()
    config.periodic_callbacks.append(_periodic)

label _tmp_verify_entry:
    $ renpy.game.preferences.skip_unseen = True
    $ renpy.game.preferences.skip_after_choices = True
    $ config.allow_skipping = True
    $ config.skipping = "fast"
    $ persistent.difficulty = "normal"
    $ player_name = "验证"
    $ persistent.chapters_completed = set()

    $ _TRACE.append("=== 从第一章开始跑全流程 ===")
    jump chapter1_start
