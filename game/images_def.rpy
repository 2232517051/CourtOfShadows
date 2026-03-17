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
## 角色立绘 - 默认表情（normal）
## ════════════════════════════════════════════════════════════

image aldric_img = Transform("images/aldric.webp", zoom=0.45, yalign=1.0)
image elena_img = Transform("images/elena.webp", zoom=0.45, yalign=1.0)
image bishop_img = Transform("images/bishop.webp", zoom=0.45, yalign=1.0)
image baron_img = Transform("images/baron.webp", zoom=0.45, yalign=1.0)
image captain_img = Transform("images/captain.webp", zoom=0.45, yalign=1.0)
image queen_img = Transform("images/queen.webp", zoom=0.45, yalign=1.0)
image merchant_karl_img = Transform("images/merchant_karl.webp", zoom=0.45, yalign=1.0)
image lily_master_img = Transform("images/lily_master.webp", zoom=0.45, yalign=1.0)
image prince_img = Transform("images/prince.webp", zoom=0.45, yalign=1.0)

## ════════════════════════════════════════════════════════════
## 角色立绘 - 表情差分（angry / sad / happy）
## 如果表情图不存在，自动回退到默认立绘
## ════════════════════════════════════════════════════════════

init python:
    # 定义所有角色和表情
    _char_expressions = {
        "aldric": ["angry", "sad", "happy"],
        "elena": ["angry", "sad", "happy"],
        "bishop": ["angry", "sad", "happy"],
        "baron": ["angry", "sad", "happy"],
        "captain": ["angry", "sad", "happy"],
        "queen": ["angry", "sad", "happy"],
        "prince": ["angry", "sad", "happy"],
        "merchant_karl": ["angry", "sad", "happy"],
        "lily_master": ["angry", "sad", "happy"],
    }

    # 直接在 init python 块中注册表情图
    for _cn, _exprs in _char_expressions.items():
        for _ex in _exprs:
            _img_tag = f"{_cn}_img_{_ex}"
            _expr_path = f"images/{_cn}_{_ex}.webp"
            _base_path = f"images/{_cn}.webp"

            if renpy.loadable(_expr_path):
                renpy.image(_img_tag, Transform(_expr_path, zoom=0.45, yalign=1.0))
            else:
                renpy.image(_img_tag, Transform(_base_path, zoom=0.45, yalign=1.0))
