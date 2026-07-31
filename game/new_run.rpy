## ============================================================
## 新周目一次性初始化
## ============================================================

default _new_run_bootstrap_done = False


label new_run_bootstrap:
    if _new_run_bootstrap_done:
        return

    $ _new_run_bootstrap_done = True

    ## 新手引导
    if not persistent.tutorial_seen:
        call screen tutorial_overlay

    ## 难度选择（每次新游戏都可选）
    call screen difficulty_select

    ## New Game+ 奖励
    $ apply_ng_plus()
    if persistent.ng_plus_unlocked:
        show screen ng_plus_banner
        pause 1.0

    ## 输入名字（自定义界面，解决手机端卡住问题）
    scene black with dissolve
    $ _name_input_value = "亚瑟"
    call screen name_input_screen
    if _return == "default":
        $ player_name = "亚瑟"
    else:
        $ player_name = _name_input_value.strip()
        if player_name == "":
            $ player_name = "亚瑟"

    ## 彩蛋名字检测
    $ _egg = check_name_easter_egg(player_name)
    if _egg:
        show screen name_easter_egg(egg_text=_egg)
        pause 2.0

    ## 初始化物品背包；保留既有存档返回点名。
    call init_inventory from _call_init_inventory_prologue

    return
