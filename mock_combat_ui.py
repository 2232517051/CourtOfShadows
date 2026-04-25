"""
生成战斗系统实机模拟截图
模拟 combat.rpy 中的战斗界面布局
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 720

# 颜色定义（与 combat.rpy 一致）
BG = (10, 8, 18)
PANEL_BG = (26, 21, 40, 144)  # #1a152890
PANEL_BG_SOLID = (26, 21, 40)
LOG_BG = (15, 13, 26, 204)
GOLD = (212, 169, 66)
TEXT_LIGHT = (224, 216, 200)
TEXT_DIM = (138, 126, 96)
TEXT_MUTED = (106, 94, 72)
RED = (231, 76, 60)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
ORANGE = (243, 156, 18)
YELLOW = (241, 196, 15)
PURPLE = (155, 89, 182)
CRIT_RED = (255, 107, 107)
HP_GREEN = (39, 174, 96)
HP_ORANGE = (230, 126, 34)
HP_RED = (192, 57, 43)
BAR_BG = (26, 21, 40)
BLEED_RED = (231, 40, 60)

img = Image.new("RGBA", (W, H), BG)
draw = ImageDraw.Draw(img)

# 尝试加载字体
font_path = os.path.join(os.path.dirname(__file__), "game", "msyh.ttf")
if not os.path.exists(font_path):
    font_path = "C:/Windows/Fonts/msyh.ttc"

def font(size):
    try:
        return ImageFont.truetype(font_path, size)
    except:
        return ImageFont.load_default()

# ─── 顶部装饰条 ───
draw.rectangle([0, 0, W, 3], fill=(212, 169, 66, 8))

# ═══════════════════════════════════════════
# 顶部：敌人信息区
# ═══════════════════════════════════════════
ex, ey = 340, 20
ew, eh = 600, 155
draw.rounded_rectangle([ex, ey, ex+ew, ey+eh], radius=6, fill=(26, 21, 40, 200))

# 敌人名字 + 难度
draw.text((ex+30, ey+15), "⚔", fill=RED, font=font(18))
draw.text((ex+55, ey+14), "教会骑士", fill=TEXT_LIGHT, font=font(20))
# 难度徽章
badge_x = ex+ew-90
draw.rounded_rectangle([badge_x, ey+14, badge_x+70, ey+34], radius=3, fill=(231, 76, 60, 48))
draw.text((badge_x+12, ey+16), "困难", fill=RED, font=font(13))

# 敌人描述
draw.text((ex+30, ey+42), "以圣光之名挥剑的虔诚战士", fill=TEXT_MUTED, font=font(13))

# 敌人HP条
draw.text((ex+30, ey+65), "HP", fill=RED, font=font(14))
hp_bar_x, hp_bar_y = ex+65, ey+67
hp_bar_w = 400
hp_pct = 0.62  # 模拟68/110
draw.rounded_rectangle([hp_bar_x, hp_bar_y, hp_bar_x+hp_bar_w, hp_bar_y+14], radius=3, fill=BAR_BG)
draw.rounded_rectangle([hp_bar_x, hp_bar_y, hp_bar_x+int(hp_bar_w*hp_pct), hp_bar_y+14], radius=3, fill=HP_RED)
draw.text((hp_bar_x+hp_bar_w+10, hp_bar_y-1), "68/110", fill=(200, 184, 144), font=font(13))

# 敌人体力条
draw.text((ex+30, ey+88), "体力", fill=BLUE, font=font(12))
st_bar_y = ey+90
st_pct = 0.45
draw.rounded_rectangle([hp_bar_x, st_bar_y, hp_bar_x+hp_bar_w, st_bar_y+8], radius=2, fill=BAR_BG)
draw.rounded_rectangle([hp_bar_x, st_bar_y, hp_bar_x+int(hp_bar_w*st_pct), st_bar_y+8], radius=2, fill=(41, 128, 185))
draw.text((hp_bar_x+hp_bar_w+10, st_bar_y-3), "疲劳", fill=ORANGE, font=font(11))

# 敌人状态标记
tag_y = ey+110
# 防御中
draw.rounded_rectangle([ex+30, tag_y, ex+110, tag_y+22], radius=3, fill=(52, 152, 219, 48))
draw.text((ex+38, tag_y+3), "🛡 防御中", fill=BLUE, font=font(11))
# 流血
draw.rounded_rectangle([ex+120, tag_y, ex+210, tag_y+22], radius=3, fill=(231, 40, 60, 48))
draw.text((ex+128, tag_y+3), "🩸 流血 2", fill=BLEED_RED, font=font(11))

# ═══════════════════════════════════════════
# 中央：战斗日志
# ═══════════════════════════════════════════
lx, ly = 330, 200
lw, lh = 620, 180
draw.rounded_rectangle([lx, ly, lx+lw, ly+lh], radius=6, fill=(15, 13, 26, 220))

# 回合标题
draw.text((lx+20, ly+12), "—", fill=(212, 169, 66, 96), font=font(12))
draw.text((lx+40, ly+10), "第 5 回合", fill=GOLD, font=font(14))
draw.text((lx+120, ly+12), "—", fill=(212, 169, 66, 96), font=font(12))

# 日志内容
logs = [
    ("你斩击攻击颈部【暴击！】—— 28伤害", TEXT_DIM),
    ("造成流血！每回合 7 伤害，持续3回合", BLEED_RED),
    ("教会骑士 摆出防御姿态，恢复体力。", TEXT_DIM),
    ("恢复能量释放！+12 体力", PURPLE),
    ("教会骑士 正在流血！失去 7 HP", BLEED_RED),
    ("你猛击攻击头部 —— 22伤害 (护甲减免)", (200, 184, 144)),
]
for i, (log, color) in enumerate(logs):
    alpha = 0.5 + 0.1 * i
    draw.text((lx+20, ly+36 + i*22), log, fill=color, font=font(13))

# ═══════════════════════════════════════════
# 浮动伤害数字
# ═══════════════════════════════════════════
draw.text((610, 155), "-22", fill=(255, 216, 102), font=font(36))

# ═══════════════════════════════════════════
# 底部左侧：玩家信息
# ═══════════════════════════════════════════
px, py = 20, 440
pw, ph = 320, 260
draw.rounded_rectangle([px, py, px+pw, py+ph], radius=6, fill=(26, 21, 40, 200))

# 玩家名
draw.text((px+18, py+12), "🛡", fill=GOLD, font=font(18))
draw.text((px+45, py+12), "艾登堡领主", fill=GOLD, font=font(18))

# HP条
draw.text((px+18, py+42), "HP", fill=RED, font=font(13))
php_x, php_y = px+50, py+44
php_w = 200
p_hp_pct = 0.78
draw.rounded_rectangle([php_x, php_y, php_x+php_w, php_y+14], radius=3, fill=BAR_BG)
draw.rounded_rectangle([php_x, php_y, php_x+int(php_w*p_hp_pct), php_y+14], radius=3, fill=HP_GREEN)
draw.text((php_x+php_w+8, php_y-1), "89/114", fill=(200, 184, 144), font=font(12))

# 体力条
draw.text((px+18, py+64), "体力", fill=BLUE, font=font(11))
pst_y = py+66
pst_pct = 0.65
draw.rounded_rectangle([php_x, pst_y, php_x+php_w, pst_y+10], radius=2, fill=BAR_BG)
draw.rounded_rectangle([php_x, pst_y, php_x+int(php_w*pst_pct), pst_y+10], radius=2, fill=(41, 128, 185))
draw.text((php_x+php_w+8, pst_y-1), "65/100", fill=TEXT_MUTED, font=font(11))

# 疲劳 + 姿态
draw.text((px+18, py+86), "疲劳:", fill=TEXT_MUTED, font=font(12))
draw.text((px+60, py+85), "略感疲惫", fill=(168, 216, 106), font=font(13))
draw.text((px+145, py+87), "|", fill=(74, 64, 48), font=font(12))
draw.text((px+160, py+85), "攻势", fill=RED, font=font(13))

# 战斗属性
attrs = [("攻18", RED), ("防12", BLUE), ("闪15%", GREEN), ("暴22%", ORANGE), ("气5", PURPLE)]
attr_x = px+18
for text, color in attrs:
    draw.text((attr_x, py+108), text, fill=color, font=font(11))
    attr_x += 55

# 状态标记
tag_x = px+18
tag_py = py+130
# 闪避
draw.rounded_rectangle([tag_x, tag_py, tag_x+65, tag_py+20], radius=3, fill=(46, 204, 113, 48))
draw.text((tag_x+6, tag_py+3), "💨 闪避", fill=GREEN, font=font(11))
# 流血
draw.rounded_rectangle([tag_x+72, tag_py, tag_x+145, tag_py+20], radius=3, fill=(231, 40, 60, 48))
draw.text((tag_x+78, tag_py+3), "🩸 流血1", fill=BLEED_RED, font=font(11))

# 受伤标记
draw.rounded_rectangle([tag_x, tag_py+26, tag_x+55, tag_py+46], radius=3, fill=(231, 76, 60, 48))
draw.text((tag_x+6, tag_py+29), "头伤", fill=RED, font=font(11))

# ═══════════════════════════════════════════
# 底部右侧：行动按钮面板
# ═══════════════════════════════════════════
ax, ay = 920, 390
aW, aH = 340, 315
draw.rounded_rectangle([ax, ay, ax+aW, ay+aH], radius=6, fill=(26, 21, 40, 200))

# 标题 + 姿态切换
draw.text((ax+16, ay+12), "⚔ 行动", fill=GOLD, font=font(15))
# 姿态按钮
stance_bx = ax+110
draw.rounded_rectangle([stance_bx, ay+10, stance_bx+80, ay+34], radius=4, fill=(231, 76, 60, 48))
draw.text((stance_bx+22, ay+14), "攻势", fill=RED, font=font(13))

# 2x4 按钮网格
btn_colors = [
    ("⚔ 斩击", "消耗10体力", (42, 31, 60), TEXT_LIGHT),
    ("🔨 猛击", "1.5x伤 消耗20", (42, 31, 60), TEXT_LIGHT),
    ("🛡 盾击", "削体+晕 消耗15", (42, 42, 26), YELLOW),
    ("🛡 防御", "减伤50% +体力", (26, 42, 60), BLUE),
    ("💨 闪避", "闪避+30% 消耗5", (26, 60, 42), GREEN),
    ("🧪 物品", "使用物品", (60, 42, 26), ORANGE),
    ("🏃 撤退", "成功率72%", (60, 26, 26), RED),
]

btn_w, btn_h = 150, 48
btn_gap = 6
btn_start_y = ay + 44
for i, (name, desc, bg, color) in enumerate(btn_colors):
    col = i % 2
    row = i // 2
    bx = ax + 16 + col * (btn_w + btn_gap)
    by = btn_start_y + row * (btn_h + btn_gap)
    draw.rounded_rectangle([bx, by, bx+btn_w, by+btn_h], radius=4, fill=bg)
    # 高亮边框（盾击按钮特殊处理）
    if i == 2:
        draw.rounded_rectangle([bx, by, bx+btn_w, by+btn_h], radius=4, outline=(241, 196, 15, 60))
    draw.text((bx+10, by+8), name, fill=color, font=font(14))
    draw.text((bx+10, by+28), desc, fill=TEXT_MUTED, font=font(9))

# 空白占位（第8格）
bx8 = ax + 16 + 1 * (btn_w + btn_gap)
by8 = btn_start_y + 3 * (btn_h + btn_gap)
# 不画

# ═══════════════════════════════════════════
# 身体部位选择面板（半透明覆盖，显示在中下方）
# ═══════════════════════════════════════════
tpx, tpy = 360, 480
tpw, tph = 560, 200
draw.rounded_rectangle([tpx, tpy, tpx+tpw, tpy+tph], radius=8, fill=(26, 21, 40, 238))

draw.text((tpx + tpw//2 - 60, tpy+12), "选择攻击部位", fill=GOLD, font=font(18))

# 4个部位按钮 (2x2)
parts = [
    ("头部", "1.5x伤 -15%命中", "可眩晕", (60, 26, 26), RED, ORANGE),
    ("颈部", "2.0x伤 -25%命中", "可流血", (74, 26, 42), CRIT_RED, BLEED_RED),
    ("躯干", "1.0x伤 标准命中", "最稳妥", (42, 42, 60), TEXT_LIGHT, TEXT_MUTED),
    ("四肢", "0.75x伤 +10%命中", "高命中", (26, 60, 42), GREEN, GREEN),
]

part_w, part_h = 130, 70
part_gap = 10
part_start_x = tpx + (tpw - 2*part_w - part_gap) // 2
part_start_y = tpy + 42

for i, (name, desc, sub, bg, nc, sc) in enumerate(parts):
    col = i % 2
    row = i // 2
    pbx = part_start_x + col * (part_w + part_gap)
    pby = part_start_y + row * (part_h + part_gap)
    draw.rounded_rectangle([pbx, pby, pbx+part_w, pby+part_h], radius=5, fill=bg)
    draw.text((pbx + part_w//2 - 12, pby+8), name, fill=nc, font=font(15))
    draw.text((pbx + 10, pby+30), desc, fill=(200, 184, 144), font=font(10))
    draw.text((pbx + 10, pby+48), sub, fill=sc, font=font(10))

# 取消按钮
draw.text((tpx + tpw//2 - 12, tpy+tph-24), "取消", fill=TEXT_MUTED, font=font(14))

# ═══════════════════════════════════════════
# 底部暗色渐变装饰
# ═══════════════════════════════════════════
for i in range(40):
    alpha = int(80 * (i / 40))
    draw.rectangle([0, H-40+i, W, H-40+i+1], fill=(15, 13, 26, alpha))

# ═══════════════════════════════════════════
# 标题水印
# ═══════════════════════════════════════════
draw.text((W-260, H-25), "权谋之庭 v3.0 · 战斗系统", fill=(106, 94, 72, 120), font=font(12))

# 保存
out_path = os.path.join(os.path.dirname(__file__), "combat_ui_mockup.png")
img = img.convert("RGB")
img.save(out_path, quality=95)
print(f"Saved: {out_path}")
print(f"Size: {os.path.getsize(out_path)} bytes")
