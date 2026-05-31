## ============================================================
## 图片定义 - 背景图 + 角色立绘（支持表情差分 & 日夜变体）
## ============================================================

init python:
    def safe_image(path, fallback=None):
        """如果图片存在则返回路径，否则返回 fallback"""
        if renpy.loadable(path):
            return path
        return fallback

## ════════════════════════════════════════════════════════════
## 背景图 - 基础版本（日间/默认）
## ════════════════════════════════════════════════════════════

image bg castle_exterior = Transform("images/bg_castle_exterior.webp", size=(1280, 720), fit="cover")
image bg great_hall = Transform("images/bg_great_hall.webp", size=(1280, 720), fit="cover")
image bg study = Transform("images/bg_study.webp", size=(1280, 720), fit="cover")
image bg border = Transform("images/bg_border.webp", size=(1280, 720), fit="cover")
image bg council_hall = Transform("images/bg_council_hall.webp", size=(1280, 720), fit="cover")
image bg market = Transform("images/bg_market.webp", size=(1280, 720), fit="cover")
image bg forest_path = Transform("images/bg_forest_path.webp", size=(1280, 720), fit="cover")
image bg underground = Transform("images/bg_underground.webp", size=(1280, 720), fit="cover")
image bg church_interior = Transform("images/bg_church_interior.webp", size=(1280, 720), fit="cover")
image bg royal_palace = Transform("images/bg_royal_palace.webp", size=(1280, 720), fit="cover")
image bg throne_room = Transform("images/bg_throne_room.webp", size=(1280, 720), fit="cover")
image bg palace_garden = Transform("images/bg_palace_garden.webp", size=(1280, 720), fit="cover")
image bg dungeon = Transform("images/bg_dungeon.webp", size=(1280, 720), fit="cover")
image bg battlefield = Transform("images/bg_battlefield.webp", size=(1280, 720), fit="cover")

## ════════════════════════════════════════════════════════════
## 背景图 - 别名映射（场景引用名 → 已有素材）
## ════════════════════════════════════════════════════════════

image bg_castle_corridor = Transform("images/bg_council_hall.webp", size=(1280, 720), fit="cover")
image bg_castle_gate = Transform("images/bg_castle_exterior.webp", size=(1280, 720), fit="cover")
image bg_road_night = Transform("images/bg_forest_path.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#667799"))
image bg_road_dawn = Transform("images/bg_forest_path.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#ffddaa"))
image bg_study_night = Transform("images/bg_study.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#667799"))
image bg_bedroom = Transform("images/bg_castle_bedchamber.webp", size=(1280, 720), fit="cover")
image bg_ancient_ruins = Transform("images/bg_ancient_ruins.webp", size=(1280, 720), fit="cover")
image bg_crypt = Transform("images/bg_crypt.webp", size=(1280, 720), fit="cover")

## 下划线别名（pv.rpy 等使用 scene bg_xxx 格式）
image bg_battlefield = Transform("images/bg_battlefield.webp", size=(1280, 720), fit="cover")
image bg_border = Transform("images/bg_border.webp", size=(1280, 720), fit="cover")
image bg_castle_exterior = Transform("images/bg_castle_exterior.webp", size=(1280, 720), fit="cover")
image bg_church_interior = Transform("images/bg_church_interior.webp", size=(1280, 720), fit="cover")
image bg_great_hall = Transform("images/bg_great_hall.webp", size=(1280, 720), fit="cover")
image bg_throne_room = Transform("images/bg_throne_room.webp", size=(1280, 720), fit="cover")
image bg_underground = Transform("images/bg_underground.webp", size=(1280, 720), fit="cover")

## 空格分隔格式别名（scene bg xxx 引用）
image bg bedroom = Transform("images/bg_castle_bedchamber.webp", size=(1280, 720), fit="cover")
image bg ancient_ruins = Transform("images/bg_ancient_ruins.webp", size=(1280, 720), fit="cover")
image bg crypt = Transform("images/bg_crypt.webp", size=(1280, 720), fit="cover")
image bg castle_garden = Transform("images/bg_palace_garden.webp", size=(1280, 720), fit="cover")
image bg castle_library = Transform("images/bg_study.webp", size=(1280, 720), fit="cover")
image bg castle_interior = Transform("images/bg_great_hall.webp", size=(1280, 720), fit="cover")
image bg cellar = Transform("images/bg_underground.webp", size=(1280, 720), fit="cover")
image bg town_market = Transform("images/bg_market.webp", size=(1280, 720), fit="cover")
image bg tavern = Transform("images/bg_market.webp", size=(1280, 720), fit="cover")
image bg player_room = Transform("images/bg_castle_bedchamber.webp", size=(1280, 720), fit="cover")
image bg marketplace = Transform("images/bg_market.webp", size=(1280, 720), fit="cover")
image bg church = Transform("images/bg_church_interior.webp", size=(1280, 720), fit="cover")
image bg village = Transform("images/bg_market.webp", size=(1280, 720), fit="cover")
image bg castle_hall = Transform("images/bg_great_hall.webp", size=(1280, 720), fit="cover")
image bg castle_chapel = Transform("images/bg_castle_chapel.webp", size=(1280, 720), fit="cover")
image bg castle_armory = Transform("images/bg_castle_armory.webp", size=(1280, 720), fit="cover")

## ── 南境游记 DLC 场景（优先用专属图 bg_tideport_*，缺失回退通用海港素材）──
image bg tideport_harbor = Transform(safe_image("images/bg_tideport_harbor.webp", "images/bg_harbor.webp"), size=(1280, 720), fit="cover")
image bg tideport_beach  = Transform(safe_image("images/bg_tideport_beach.webp", "images/bg_beach.webp"), size=(1280, 720), fit="cover")
image bg tideport_tavern = Transform(safe_image("images/bg_tideport_tavern.webp", "images/bg_tavern.webp"), size=(1280, 720), fit="cover")
image bg tideport_ship   = Transform(safe_image("images/bg_tideport_ship.webp", "images/bg_beach.webp"), size=(1280, 720), fit="cover")
image bg tideport_office = Transform(safe_image("images/bg_tideport_office.webp", "images/bg_study.webp"), size=(1280, 720), fit="cover")
image bg tideport_fleet  = Transform(safe_image("images/bg_tideport_fleet.webp", "images/bg_harbor.webp"), size=(1280, 720), fit="cover")

## ════════════════════════════════════════════════════════════
## 背景图 - 夜间变体（如果图片存在则使用专用夜景，否则用色调叠加模拟）
## ════════════════════════════════════════════════════════════

image bg castle_exterior_night = ConditionSwitch(
    "renpy.loadable('images/bg_castle_exterior_night.webp')",
    Transform("images/bg_castle_exterior_night.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_castle_exterior.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#8899cc"))
)

image bg border_night = ConditionSwitch(
    "renpy.loadable('images/bg_border_night.webp')",
    Transform("images/bg_border_night.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_border.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#8899cc"))
)

image bg market_night = ConditionSwitch(
    "renpy.loadable('images/bg_market_night.webp')",
    Transform("images/bg_market_night.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_market.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#8899cc"))
)

image bg battlefield_night = ConditionSwitch(
    "renpy.loadable('images/bg_battlefield_night.webp')",
    Transform("images/bg_battlefield_night.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_battlefield.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#8899cc"))
)

image bg royal_palace_night = ConditionSwitch(
    "renpy.loadable('images/bg_royal_palace_night.webp')",
    Transform("images/bg_royal_palace_night.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_royal_palace.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#8899cc"))
)

## ════════════════════════════════════════════════════════════
## 背景图 - 黄昏变体
## ════════════════════════════════════════════════════════════

image bg castle_exterior_dusk = ConditionSwitch(
    "renpy.loadable('images/bg_castle_exterior_dusk.webp')",
    Transform("images/bg_castle_exterior_dusk.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_castle_exterior.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#ffcc88"))
)

image bg border_dusk = ConditionSwitch(
    "renpy.loadable('images/bg_border_dusk.webp')",
    Transform("images/bg_border_dusk.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_border.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#ffcc88"))
)

image bg palace_garden_dusk = ConditionSwitch(
    "renpy.loadable('images/bg_palace_garden_dusk.webp')",
    Transform("images/bg_palace_garden_dusk.webp", size=(1280, 720), fit="cover"),
    "True",
    Transform("images/bg_palace_garden.webp", size=(1280, 720), fit="cover", matrixcolor=TintMatrix("#ffcc88"))
)

## ════════════════════════════════════════════════════════════
## 角色立绘 - 默认表情（normal）- 全身用于 show
## ════════════════════════════════════════════════════════════

## 核心角色
image aldric_img = Transform("images/aldric.png", zoom=0.45, yalign=1.0)
## 艾琳娜立绘演化 (batch 5 "云"反馈, 2026-05-11):
## rel_elena >= 80 或 elena_romance 时切换"亲密版" (表情柔和 + 脸颊微红 + 嘴角轻笑)
## 服装/发型/姿势/背景完全一致, 变化 subtle 但表达"她把面具卸下来了"
image elena_img = ConditionSwitch(
    "rel_elena >= 80 or elena_romance", Transform("images/elena_intimate.png", zoom=0.45, yalign=1.0),
    "True", Transform("images/elena.png", zoom=0.45, yalign=1.0))
image bishop_img = Transform("images/bishop.png", zoom=0.45, yalign=1.0)
image baron_img = Transform("images/baron.png", zoom=0.45, yalign=1.0)
image captain_img = Transform("images/captain.png", zoom=0.45, yalign=1.0)
image queen_img = Transform("images/queen.png", zoom=0.45, yalign=1.0)
image merchant_karl_img = Transform("images/merchant_karl.png", zoom=0.45, yalign=1.0)
image lily_master_img = Transform("images/lily_master.png", zoom=0.45, yalign=1.0)
image prince_img = Transform("images/prince.png", zoom=0.45, yalign=1.0)

## 南境游记 DLC — 渡鸦船长赛琳
## 仿 Elena：rel_corsair>=80 或 corsair_romance 时切"亲密版"；亲密图未生成时回退基础立绘。
image corsair_img = ConditionSwitch(
    "(rel_corsair >= 80 or corsair_romance) and renpy.loadable('images/corsair_intimate.png')",
        Transform("images/corsair_intimate.png", zoom=0.45, yalign=1.0),
    "True",
        Transform(safe_image("images/corsair.png", "images/noble_lady.png"), zoom=0.45, yalign=1.0))

## 南境游记 DLC 配角(专属图待生成时回退原占位)
image guild_master_img = Transform(safe_image("images/guild_master.png", "images/merchant_guild.png"), zoom=0.45, yalign=1.0)
image ship_boy_img = Transform(safe_image("images/ship_boy.png", "images/servant_generic.png"), zoom=0.45, yalign=1.0)
image dockhand_img = Transform(safe_image("images/dockhand.png", "images/servant_generic.png"), zoom=0.45, yalign=1.0)

## 序章角色
image mother_img = Transform("images/mother.png", zoom=0.45, yalign=1.0)
image father_img = Transform("images/father.png", zoom=0.45, yalign=1.0)
image tutor_img = Transform("images/tutor.png", zoom=0.45, yalign=1.0)
image friend_marcus_img = Transform("images/friend_marcus.png", zoom=0.45, yalign=1.0)
image bully_kid_img = Transform("images/bully_kid.png", zoom=0.45, yalign=1.0)
image old_guard_img = Transform("images/old_guard.png", zoom=0.45, yalign=1.0)
image servant_marta_img = Transform("images/servant_marta.png", zoom=0.45, yalign=1.0)
image priest_thomas_img = Transform("images/priest_thomas.png", zoom=0.45, yalign=1.0)
image noble_werner_img = Transform("images/noble_werner.png", zoom=0.45, yalign=1.0)
image countess_hilda_img = Transform("images/countess_hilda.png", zoom=0.45, yalign=1.0)

## 第二章会前交际角色
image count_grey_img = Transform("images/count_grey.png", zoom=0.45, yalign=1.0)
image viscount_wells_img = Transform("images/viscount_wells.png", zoom=0.45, yalign=1.0)
image countess_stein_img = Transform("images/countess_stein.png", zoom=0.45, yalign=1.0)
image storyteller_img = Transform("images/storyteller.png", zoom=0.45, yalign=1.0)
image assassin_char_img = Transform("images/assassin_char.png", zoom=0.45, yalign=1.0)

## 通用角色
image blacksmith_wife_img = Transform("images/blacksmith_wife.png", zoom=0.45, yalign=1.0)
image noble_lady_img = Transform("images/noble_lady.png", zoom=0.45, yalign=1.0)
image soldier_generic_img = Transform("images/soldier_generic.png", zoom=0.45, yalign=1.0)
image servant_generic_img = Transform("images/servant_generic.png", zoom=0.45, yalign=1.0)
image old_woman_img = Transform("images/old_woman.png", zoom=0.45, yalign=1.0)
image herbalist_vera_img = Transform("images/herbalist_vera.png", zoom=0.45, yalign=1.0)
image lily_root_img = Transform("images/lily_root.png", zoom=0.45, yalign=1.0)
image queen_envoy_img = Transform("images/queen_envoy.png", zoom=0.45, yalign=1.0)
image stable_boy_img = Transform("images/stable_boy.png", zoom=0.45, yalign=1.0)
image herald_img = Transform("images/herald.png", zoom=0.45, yalign=1.0)
image beggar_img = Transform("images/beggar.png", zoom=0.45, yalign=1.0)
image court_herald_img = Transform("images/court_herald.png", zoom=0.45, yalign=1.0)
image court_poet_img = Transform("images/court_poet.png", zoom=0.45, yalign=1.0)

## 序章特殊角色
image bertrand_img = Transform("images/bertrand.png", zoom=0.45, yalign=1.0)

## 治理/NPC角色（新生成）
image farmer_rep_img = Transform("images/farmer_rep.png", zoom=0.45, yalign=1.0)
image healer_img = Transform("images/healer.png", zoom=0.45, yalign=1.0)
image merchant_guild_img = Transform("images/merchant_guild.png", zoom=0.45, yalign=1.0)
image tax_collector_img = Transform("images/tax_collector.png", zoom=0.45, yalign=1.0)
image village_elder_img = Transform("images/village_elder.png", zoom=0.45, yalign=1.0)

## 主角 (各时期)
## chapter3 遇刺后立绘自动切换"带疤版" (canon: chapter3.rpy:25/1299/1706)
## 通过 ConditionSwitch + player_scarred flag 自动切换, 不需要改任何 show 调用
image player_char_img = ConditionSwitch(
    "player_scarred", Transform("images/player_char_scarred.png", zoom=0.45, yalign=1.0),
    "True", Transform("images/player_char.png", zoom=0.45, yalign=1.0),
)
image player_char_img angry = ConditionSwitch(
    "player_scarred", Transform("images/player_char_scarred_angry.png", zoom=0.45, yalign=1.0),
    "True", Transform("images/player_char_angry.png", zoom=0.45, yalign=1.0),
)
image player_char_img happy = ConditionSwitch(
    "player_scarred", Transform("images/player_char_scarred_happy.png", zoom=0.45, yalign=1.0),
    "True", Transform("images/player_char_happy.png", zoom=0.45, yalign=1.0),
)
image player_char_img sad = ConditionSwitch(
    "player_scarred", Transform("images/player_char_scarred_sad.png", zoom=0.45, yalign=1.0),
    "True", Transform("images/player_char_sad.png", zoom=0.45, yalign=1.0),
)
image player_child_img = Transform("images/player_child.png", zoom=0.45, yalign=1.0)
image player_teen_img = Transform("images/player_teen.png", zoom=0.45, yalign=1.0)
image player_young_img = Transform("images/player_young.png", zoom=0.45, yalign=1.0)

## ════════════════════════════════════════════════════════════
## 角色肖像 - side image (对话框旁自动显示头像)
## 裁剪为头部区域，缩放到合适的对话框大小
## ════════════════════════════════════════════════════════════

init python:
    # 所有有立绘的角色ID列表
    _all_portrait_chars = [
        "aldric", "elena", "bishop", "baron", "captain", "queen",
        "merchant_karl", "lily_master", "prince",
        "mother", "father", "tutor", "friend_marcus", "bully_kid",
        "old_guard", "servant_marta", "priest_thomas", "noble_werner",
        "countess_hilda", "count_grey", "viscount_wells", "countess_stein",
        "storyteller", "assassin_char", "blacksmith_wife", "noble_lady",
        "soldier_generic", "servant_generic", "old_woman",
        "herbalist_vera", "lily_root", "queen_envoy", "stable_boy",
        "herald", "beggar", "court_herald", "court_poet",
        # 序章特殊角色
        "bertrand",
        # 治理/NPC角色
        "farmer_rep", "healer", "merchant_guild", "tax_collector", "village_elder",
        # 主角 (成年/童年/少年/青年)
        "player_char", "player_child", "player_teen", "player_young",
        # 南境游记 DLC
        "corsair", "guild_master", "ship_boy", "dockhand",
    ]

    # 为每个角色注册 side image (默认 + 表情差分)
    # 完整立绘缩放到对话框高度 (不裁剪，保持完整图片)
    # 768x1024 → 165x220
    _side_size = (165, 220)
    for _cn in _all_portrait_chars:
        # 默认 side image
        _base_path = f"images/{_cn}.png"
        if renpy.loadable(_base_path):
            renpy.image(f"side {_cn}", Transform(_base_path, size=_side_size))

        # 表情差分 side image
        for _ex in ["angry", "sad", "happy"]:
            _expr_path = f"images/{_cn}_{_ex}.png"
            if renpy.loadable(_expr_path):
                renpy.image(f"side {_cn} {_ex}", Transform(_expr_path, size=_side_size))
            elif renpy.loadable(_base_path):
                renpy.image(f"side {_cn} {_ex}", Transform(_base_path, size=_side_size))

## ════════════════════════════════════════════════════════════
## 角色立绘 - 表情差分（angry / sad / happy）- 全身用于 show
## 如果表情图不存在，自动回退到默认立绘
## ════════════════════════════════════════════════════════════

init python:
    # 定义所有角色和表情
    _expr_list = ["angry", "sad", "happy"]
    _char_expressions = {_cn: _expr_list for _cn in _all_portrait_chars}

    # 直接在 init python 块中注册表情图
    # 使用空格分隔（如 "baron_img angry"）使表情变体与基础立绘共享同一 tag
    # 这样 show baron_img angry 会自动替换 show baron_img，不会重叠
    for _cn, _exprs in _char_expressions.items():
        for _ex in _exprs:
            _img_tag = f"{_cn}_img {_ex}"
            _expr_path = f"images/{_cn}_{_ex}.png"
            _base_path = f"images/{_cn}.png"

            if renpy.loadable(_expr_path):
                renpy.image(_img_tag, Transform(_expr_path, zoom=0.45, yalign=1.0))
            else:
                renpy.image(_img_tag, Transform(_base_path, zoom=0.45, yalign=1.0))
