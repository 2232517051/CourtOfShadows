## ============================================================
## 制作系统 - Crafting System
## crafting.rpy
## 使用背包素材合成物品
## ============================================================

## ── 制作追踪变量 ──
default crafting_skill_bonus = 0
default total_items_crafted = 0

init python:

    ## ================================================================
    ## 配方数据库
    ## ================================================================

    crafting_recipes = {
        "health_potion": {
            "name": "治疗药水",
            "icon": "药",
            "icon_color": "#2ecc71",
            "desc": "恢复生命值的草药配制药水，战斗中的救命良药。",
            "materials": {"medicinal_herbs": 2, "waterskin": 1},
            "skill_req": 0,
            "result_qty": 1,
            "result_id": "health_potion",
            "category": "药剂",
        },
        "stamina_potion": {
            "name": "耐力药水",
            "icon": "耐",
            "icon_color": "#3498db",
            "desc": "混合圣水与药草的提神饮品，恢复体力和精神。",
            "materials": {"medicinal_herbs": 1, "holy_water": 1},
            "skill_req": 10,
            "result_qty": 1,
            "result_id": "stamina_potion",
            "category": "药剂",
        },
        "antidote": {
            "name": "解毒药",
            "icon": "解",
            "icon_color": "#9b59b6",
            "desc": "以毒攻毒的解药，使用暗百合提取物中和体内毒素。",
            "materials": {"medicinal_herbs": 3, "dark_lily_extract": 1},
            "skill_req": 20,
            "result_qty": 1,
            "result_id": "antidote",
            "category": "药剂",
        },
        "bandage": {
            "name": "绷带",
            "icon": "绷",
            "icon_color": "#ecf0f1",
            "desc": "用皮革裁剪的简易绷带，可以止血包扎伤口。",
            "materials": {"leather_scraps": 2},
            "skill_req": 0,
            "result_qty": 2,
            "result_id": "bandage",
            "category": "药剂",
        },
        "war_paint": {
            "name": "战争涂料",
            "icon": "战",
            "icon_color": "#e74c3c",
            "desc": "铁粉与草药混合的涂料，涂抹面部可暂时提升士气和战意。",
            "materials": {"iron_ore": 1, "medicinal_herbs": 1},
            "skill_req": 15,
            "result_qty": 1,
            "result_id": "war_paint",
            "category": "战斗",
        },
        "smoke_bomb": {
            "name": "烟雾弹",
            "icon": "烟",
            "icon_color": "#7f8c8d",
            "desc": "铁壳包裹的发烟装置，破裂后释放浓烟，用于掩护或逃脱。",
            "materials": {"iron_ore": 2, "dark_lily_extract": 1},
            "skill_req": 25,
            "result_qty": 1,
            "result_id": "smoke_bomb",
            "category": "战斗",
        },
        "gambeson": {
            "name": "棉甲",
            "icon": "甲",
            "icon_color": "#d2691e",
            "desc": "多层皮革缝制的软甲，轻便灵活，提供基础防护。",
            "materials": {"leather_scraps": 4, "iron_ore": 1},
            "skill_req": 20,
            "result_qty": 1,
            "result_id": "gambeson",
            "category": "装备",
        },
        "chainmail": {
            "name": "锁子甲",
            "icon": "锁",
            "icon_color": "#bdc3c7",
            "desc": "由数千个铁环编织而成的重甲，防护力极强。",
            "materials": {"iron_ore": 5, "leather_scraps": 2},
            "skill_req": 40,
            "result_qty": 1,
            "result_id": "chainmail",
            "category": "装备",
        },
        "blessed_mace": {
            "name": "祝福战锤",
            "icon": "锤",
            "icon_color": "#ffd700",
            "desc": "以圣水淬炼的铁锤，据说对邪恶之物有特殊效果。",
            "materials": {"iron_ore": 3, "holy_water": 2},
            "skill_req": 35,
            "result_qty": 1,
            "result_id": "blessed_mace",
            "category": "装备",
        },
        "potent_medicine": {
            "name": "强效药剂",
            "icon": "强",
            "icon_color": "#e67e22",
            "desc": "复杂配方的高级药剂，治疗效果远超普通药水。",
            "materials": {"medicinal_herbs": 2, "holy_water": 1, "waterskin": 1},
            "skill_req": 30,
            "result_qty": 1,
            "result_id": "potent_medicine",
            "category": "药剂",
        },
    }

    ## ================================================================
    ## 制作核心函数
    ## ================================================================

    def get_crafting_skill():
        """获取制作技能值 = 谋略 * 0.6 + 额外加成"""
        base = int(store.intrigue * 0.6)
        bonus = store.crafting_skill_bonus if hasattr(store, 'crafting_skill_bonus') else 0
        return min(100, base + bonus)

    def get_success_rate(recipe_id):
        """计算制作成功率"""
        recipe = crafting_recipes.get(recipe_id)
        if not recipe:
            return 0
        skill = get_crafting_skill()
        ## 基础成功率: 70% + 技能 * 0.5, 上限95%
        rate = 70 + skill * 0.5
        ## 技能不足时降低成功率
        if skill < recipe["skill_req"]:
            penalty = (recipe["skill_req"] - skill) * 2
            rate -= penalty
        return max(10, min(95, int(rate)))

    def can_craft(recipe_id):
        """检查是否有足够材料（不检查技能门槛——技能不足也可以尝试，只是成功率低）"""
        recipe = crafting_recipes.get(recipe_id)
        if not recipe:
            return False
        inv = get_inventory()
        for mat_id, mat_qty in recipe["materials"].items():
            if inv.get(mat_id, 0) < mat_qty:
                return False
        return True

    def get_missing_materials(recipe_id):
        """返回缺少的材料列表 [(物品id, 需要量， 拥有量)]"""
        recipe = crafting_recipes.get(recipe_id)
        if not recipe:
            return []
        inv = get_inventory()
        missing = []
        for mat_id, mat_qty in recipe["materials"].items():
            have = inv.get(mat_id, 0)
            if have < mat_qty:
                missing.append((mat_id, mat_qty, have))
        return missing

    def do_craft(recipe_id):
        """
        执行制作。
        返回: ("success", qty) / ("critical", qty) / ("failure", lost_mats)
        """
        recipe = crafting_recipes.get(recipe_id)
        if not recipe:
            return ("failure", [])

        if not can_craft(recipe_id):
            return ("failure", [])

        skill = get_crafting_skill()
        rate = get_success_rate(recipe_id)
        roll = renpy.random.randint(1, 100)

        ## 消耗材料
        materials_consumed = []
        for mat_id, mat_qty in recipe["materials"].items():
            materials_consumed.append((mat_id, mat_qty))

        if roll <= rate:
            ## 成功！消耗所有材料
            for mat_id, mat_qty in materials_consumed:
                remove_item(mat_id, mat_qty)

            ## 暴击判定: 技能 > 30 时有 10% 概率
            crit_roll = renpy.random.randint(1, 100)
            if skill > 30 and crit_roll <= 10:
                ## 暴击！双倍产出
                result_qty = recipe["result_qty"] * 2
                add_item(recipe["result_id"], result_qty)
                store.total_items_crafted += result_qty
                return ("critical", result_qty)
            else:
                result_qty = recipe["result_qty"]
                add_item(recipe["result_id"], result_qty)
                store.total_items_crafted += result_qty
                return ("success", result_qty)
        else:
            ## 失败！损失50%的材料
            lost = []
            for mat_id, mat_qty in materials_consumed:
                lost_qty = max(1, mat_qty // 2)
                remove_item(mat_id, lost_qty)
                if mat_id in _item_data:
                    lost.append((_item_data[mat_id][0], lost_qty))
            return ("failure", lost)


## ================================================================
## 制作界面
## ================================================================

screen crafting_screen():
    ## 去掉 tag menu — 避免与Ren'Py内置游戏菜单冲突，否则关闭后UI失效
    modal True
    zorder 150

    ## 选中的配方
    default selected_recipe = None

    add Solid("#000000aa") at stats_overlay_show
    key "K_ESCAPE" action Hide("crafting_screen")
    key "game_menu" action Hide("crafting_screen")

    frame at stats_panel_show:
        xalign 0.5
        yalign 0.5
        xpadding 0
        ypadding 0
        if renpy.variant("small"):
            xsize 0.98
            ysize 0.92
        else:
            xsize 800
            ysize 600

        background Solid("#0f0d1af0")

        vbox:
            spacing 0

            ## ── 标题栏 ──
            frame:
                xfill True
                ysize 60
                background Solid("#1a1528")
                xpadding 24

                hbox:
                    yalign 0.5
                    xfill True

                    hbox:
                        spacing 10
                        text "锤" size 22 color "#d4a942" yalign 0.5
                        text "制作工坊" size 24 color "#d4a942" font "msyh.ttf" bold True yalign 0.5

                    hbox:
                        xalign 1.0
                        spacing 12

                        ## 制作技能显示
                        $ _cs = get_crafting_skill()
                        text "技能： [_cs]" size 14 color "#8a7e60" yalign 0.5

                        textbutton "X":
                            text_size 20
                            text_color "#6a5e48"
                            text_hover_color "#d4a942"
                            action Hide("crafting_screen")

            add Solid("#d4a94230") xsize 1.0 ysize 2

            ## ── 主内容区: 左右分栏 ──
            hbox:
                spacing 0
                xfill True

                ## ════════════════════════════════
                ## 左栏: 配方列表
                ## ════════════════════════════════
                frame:
                    if renpy.variant("small"):
                        xsize 0.45
                    else:
                        xsize 340
                    yfill True
                    background Solid("#0a081200")
                    xpadding 0
                    ypadding 0

                    vbox:
                        spacing 0

                        frame:
                            xfill True
                            ysize 36
                            xpadding 16
                            background Solid("#1a152830")
                            text "配方列表" size 14 color "#8a7e60" font "msyh.ttf" yalign 0.5

                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            draggable True
                            scrollbars "vertical"

                            frame:
                                background None
                                xpadding 8
                                ypadding 8

                                vbox:
                                    spacing 2

                                    ## 按类别分组
                                    for _rc_cat, _rc_label in [("药剂", "药剂"), ("战斗", "战斗用品"), ("装备", "装备")]:
                                        $ _rc_items = [(rid, r) for rid, r in crafting_recipes.items() if r.get("category", "") == _rc_cat]

                                        if _rc_items:
                                            text "* [_rc_label]" size 13 color "#6a5e48" font "msyh.ttf"
                                            null height 2

                                            for _rid, _rdata in _rc_items:
                                                $ _r_can = can_craft(_rid)
                                                $ _r_skill = get_crafting_skill()
                                                $ _r_skill_ok = _r_skill >= _rdata["skill_req"]
                                                $ _r_selected = (selected_recipe == _rid)

                                                ## 状态颜色
                                                if _r_can and _r_skill_ok:
                                                    $ _r_status_color = "#2ecc71"
                                                elif _r_can and not _r_skill_ok:
                                                    $ _r_status_color = "#e67e22"
                                                else:
                                                    $ _r_status_color = "#e74c3c60"

                                                button:
                                                    xfill True
                                                    xpadding 10
                                                    ypadding 8
                                                    if _r_selected:
                                                        background Solid("#d4a94220")
                                                    else:
                                                        background Solid("#1a152820")
                                                    hover_background Solid("#1a152860")
                                                    action SetScreenVariable("selected_recipe", _rid)

                                                    hbox:
                                                        spacing 8
                                                        yalign 0.5
                                                        xfill True

                                                        ## 图标
                                                        frame:
                                                            xsize 28
                                                            ysize 28
                                                            background Solid(_rdata["icon_color"] + "20")
                                                            text _rdata["icon"] xalign 0.5 yalign 0.5 size 14 color _rdata["icon_color"]

                                                        ## 名称
                                                        vbox:
                                                            text _rdata["name"] size 14 color ("#e0d8c8" if _r_can else "#6a5e48") font "msyh.ttf"
                                                            $ _r_rate = get_success_rate(_rid)
                                                            text "成功率 [_r_rate]%" size 10 color _r_status_color

                                                        ## 状态点
                                                        text "*" size 10 color _r_status_color xalign 1.0 yalign 0.5

                                            null height 6

                ## 右侧分隔线
                add Solid("#d4a94220") xsize 1 ysize 1.0

                ## ════════════════════════════════
                ## 右栏: 配方详情
                ## ════════════════════════════════
                frame:
                    xfill True
                    yfill True
                    background None
                    xpadding 0
                    ypadding 0

                    if selected_recipe is None:
                        ## 未选择配方
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 8
                            text "锤" size 40 color "#1a1528" xalign 0.5
                            text "选择一个配方" size 16 color "#6a5e48" font "msyh.ttf" xalign 0.5
                            text "查看详细信息" size 12 color "#4a4030" xalign 0.5
                    else:
                        $ _sel = crafting_recipes[selected_recipe]
                        $ _sel_can = can_craft(selected_recipe)
                        $ _sel_rate = get_success_rate(selected_recipe)
                        $ _sel_skill = get_crafting_skill()
                        $ _sel_skill_ok = _sel_skill >= _sel["skill_req"]
                        $ _sel_skill_req = _sel["skill_req"]
                        $ _sel_result_qty = _sel["result_qty"]

                        viewport:
                            xfill True
                            yfill True
                            mousewheel True
                            draggable True

                            frame:
                                background None
                                xpadding 20
                                ypadding 16
                                xfill True

                                vbox:
                                    spacing 12

                                    ## 配方名称
                                    hbox:
                                        spacing 10
                                        frame:
                                            xsize 44
                                            ysize 44
                                            background Solid(_sel["icon_color"] + "25")
                                            text _sel["icon"] xalign 0.5 yalign 0.5 size 22 color _sel["icon_color"]

                                        vbox:
                                            text _sel["name"] size 22 color "#d4a942" font "msyh.ttf" bold True
                                            text _sel.get("category", "其他") size 12 color "#6a5e48"

                                    ## 描述
                                    text _sel["desc"] size 14 color "#c8b890" font "msyh.ttf" line_spacing 4

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## 所需材料
                                    text "所需材料：" size 15 color "#d4a942" font "msyh.ttf"

                                    for _mat_id, _mat_qty in _sel["materials"].items():
                                        $ _mat_have = get_item_count(_mat_id)
                                        $ _mat_enough = _mat_have >= _mat_qty
                                        $ _mat_name = _item_data[_mat_id][0] if _mat_id in _item_data else _mat_id
                                        $ _mat_icon = _item_data[_mat_id][2] if _mat_id in _item_data else "?"

                                        hbox:
                                            spacing 8
                                            yalign 0.5

                                            frame:
                                                xsize 24
                                                ysize 24
                                                background Solid("#d4a94210")
                                                text _mat_icon xalign 0.5 yalign 0.5 size 12 color ("#d4a942" if _mat_enough else "#e74c3c60")

                                            text _mat_name size 14 color ("#e0d8c8" if _mat_enough else "#6a5e4880") font "msyh.ttf" xsize 120

                                            if _mat_enough:
                                                text "[_mat_have]/[_mat_qty]" size 14 color "#2ecc71" bold True
                                            else:
                                                text "[_mat_have]/[_mat_qty]" size 14 color "#e74c3c" bold True

                                    add Solid("#d4a94220") xsize 1.0 ysize 1

                                    ## 技能需求与成功率
                                    hbox:
                                        spacing 20

                                        vbox:
                                            spacing 2
                                            text "技能需求" size 12 color "#8a7e60"
                                            if _sel_skill_ok:
                                                text "[_sel_skill_req] (当前 [_sel_skill])" size 14 color "#2ecc71"
                                            else:
                                                text "[_sel_skill_req] (当前 [_sel_skill])" size 14 color "#e67e22"

                                        vbox:
                                            spacing 2
                                            text "成功率" size 12 color "#8a7e60"
                                            if _sel_rate >= 80:
                                                $ _rate_color = "#2ecc71"
                                            elif _sel_rate >= 50:
                                                $ _rate_color = "#e67e22"
                                            else:
                                                $ _rate_color = "#e74c3c"
                                            text "[_sel_rate]%" size 14 color _rate_color bold True

                                        vbox:
                                            spacing 2
                                            text "产出" size 12 color "#8a7e60"
                                            text "x[_sel_result_qty]" size 14 color "#d4a942" bold True

                                    ## 成功率进度条
                                    bar:
                                        value StaticValue(_sel_rate, 100)
                                        xfill True
                                        ysize 8
                                        if _sel_rate >= 80:
                                            left_bar Solid("#2ecc71")
                                        elif _sel_rate >= 50:
                                            left_bar Solid("#e67e22")
                                        else:
                                            left_bar Solid("#e74c3c")
                                        right_bar Solid("#1a1528")

                                    null height 4

                                    ## 提示
                                    if _sel_skill > 30:
                                        text "技能 > 30 时有 10% 概率暴击（双倍产出）" size 11 color "#6a5e48"
                                    if not _sel_can:
                                        text "！ 材料不足，无法制作" size 12 color "#e74c3c"
                                    elif not _sel_skill_ok:
                                        text "！ 技能不足，成功率降低" size 12 color "#e67e22"
                                    if not _sel_can:
                                        ## 显示缺少的材料
                                        $ _missing = get_missing_materials(selected_recipe)
                                        for _miss_id, _miss_need, _miss_have in _missing:
                                            $ _miss_name = _item_data[_miss_id][0] if _miss_id in _item_data else _miss_id
                                            text "  缺少 [_miss_name]: 需要[_miss_need]，拥有[_miss_have]" size 11 color "#e74c3c80"

                                    null height 8

                                    ## 制作按钮
                                    if _sel_can:
                                        textbutton "锤 制作":
                                            xalign 0.5
                                            xpadding 40
                                            ypadding 10
                                            background Solid("#d4a94230")
                                            hover_background Solid("#d4a94250")
                                            text_size 18
                                            text_color "#d4a942"
                                            text_hover_color "#ffd866"
                                            text_font "msyh.ttf"
                                            action Return(("craft", selected_recipe))
                                    else:
                                        frame:
                                            xalign 0.5
                                            xpadding 40
                                            ypadding 10
                                            background Solid("#1a152830")
                                            text "材料不足" size 16 color "#6a5e4880" font "msyh.ttf" xalign 0.5


## ================================================================
## 制作结果弹窗
## ================================================================

screen crafting_result_screen(recipe_name="", result_type="success", result_qty=0, lost_mats=None):
    zorder 310
    modal True

    add Solid("#0a0812cc")

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 36
        ypadding 28
        xminimum 380
        background Solid("#0f0d1af8")

        vbox:
            spacing 14
            xalign 0.5

            if result_type == "critical":
                text "暴击！" size 28 color "#ffd700" font "msyh.ttf" bold True xalign 0.5
                text "制作大成功！" size 16 color "#ffd700" font "msyh.ttf" xalign 0.5
                null height 4
                text "获得 [recipe_name] x[result_qty]" size 18 color "#2ecc71" font "msyh.ttf" xalign 0.5
                text "（双倍产出！）" size 14 color "#ffd700" xalign 0.5

            elif result_type == "success":
                text "制作成功" size 26 color "#2ecc71" font "msyh.ttf" bold True xalign 0.5
                null height 4
                text "获得 [recipe_name] x[result_qty]" size 18 color "#2ecc71" font "msyh.ttf" xalign 0.5

            else:
                text "制作失败" size 26 color "#e74c3c" font "msyh.ttf" bold True xalign 0.5
                text "手艺不精，制作失败了……" size 14 color "#8a7e60" xalign 0.5
                null height 4
                text "损失了部分材料：" size 14 color "#e67e22" font "msyh.ttf" xalign 0.5
                if lost_mats:
                    for _lm_name, _lm_qty in lost_mats:
                        text "  [_lm_name] x[_lm_qty]" size 14 color "#e74c3c"

            null height 8
            add Solid("#d4a94220") xsize 280 ysize 1 xalign 0.5
            null height 4

            textbutton "确定":
                xalign 0.5
                text_size 18
                text_color "#d4a942"
                text_hover_color "#ffd866"
                text_font "msyh.ttf"
                action Return()
            key "K_ESCAPE" action Return()
            key "K_RETURN" action Return()
            key "game_menu" action Return()


## ================================================================
## 制作交互标签
## ================================================================

label open_crafting:
    ## 打开制作界面的循环
    label .loop:
        call screen crafting_screen()

        $ _craft_return = _return

        if isinstance(_craft_return, tuple) and _craft_return[0] == "craft":
            $ _craft_recipe_id = _craft_return[1]
            $ _craft_recipe = crafting_recipes.get(_craft_recipe_id, {})
            $ _craft_result = do_craft(_craft_recipe_id)

            if _craft_result[0] == "critical":
                call screen crafting_result_screen(recipe_name=_craft_recipe["name"], result_type="critical", result_qty=_craft_result[1])
            elif _craft_result[0] == "success":
                call screen crafting_result_screen(recipe_name=_craft_recipe["name"], result_type="success", result_qty=_craft_result[1])
            else:
                call screen crafting_result_screen(recipe_name=_craft_recipe["name"], result_type="failure", lost_mats=_craft_result[1])

            jump open_crafting.loop

    return


## ================================================================
## 快捷方式：在脚本中调用
## ================================================================
## 用法 1 (标签调用):
##     call open_crafting
##
## 用法 2 (直接显示界面):
##     show screen crafting_screen
##
## 用法 3 (Python调用):
##     $ renpy.call("open_crafting")
