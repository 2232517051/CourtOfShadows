# -*- coding: utf-8 -*-
"""《权谋之庭》TapTap 宣传片装配线。
与实机录屏明确区分: 美术资产静帧 + Ken Burns 运镜 + 大字卡 + 叠化 + OST,
成片是"预告片"语言, 不含任何引擎 UI/对话框/菜单画面。

用法: python make_trailer.py [--cards-only]   (字卡文案在 CARDS 里, copywriter 交付后替换)
输出: <PROJ>/store_assets/trailer_v392.mp4  (1080p30, H.264+AAC)
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

PROJ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
WORK = os.path.join(os.environ.get("TEMP", "."), "cos_trailer_work")
OUT = os.path.join(PROJ, "store_assets", "trailer_v392.mp4")
## 字体必须用系统全量 msyh.ttc, **不能用 game/msyh.ttf** —— 后者被 prepare_release.py
## 子集化到只含游戏正文出现过的字。宣传文案的用字不在游戏语料里("豺"就中招了,
## 与 CLAUDE.md 记的"栀子缺字"同类)。预告片不进游戏包, 没有任何理由用子集。
FONT = r"C:/Windows/Fonts/msyh.ttc"
W, H, FPS = 1920, 1080, 30
XFADE = 0.7
# Keep the final slogan below the cover wordmark while anchoring the CTA above
# mobile-player chrome and common edge cropping.
FINAL_CARD_MAIN_Y_TOP = 875
FINAL_CARD_SUBTITLE_Y = 962
FINAL_CARD_WORDMARK_SAFE_TOP = 884
FINAL_CARD_MIN_COPY_GAP = 16
FINAL_CARD_BOTTOM_SAFE_MARGIN = 72

## 字卡 v2: 用户点名解除文风约束("直接用 opus-4.6 自己的能力"), 本版是无戒律产出。
## 主会话只做了事实核对与 A/B 选稿: 2B"意外"不合 canon(官方说法是病故)、4B"旧债"无出处、
## 6B"王座已空"不准(王座上有王后) —— 三处均选 A。文字未经任何改动。
CARDS = [
    (["丧钟未歇，豺狼已至"], None),
    (["父亲死在这把椅子上"], None),
    ## 卡3 终稿: 用户在 5 版重写中亲自选定 C2("满盘皆输")。
    (["每句话都是筹码，说错一句满盘皆输"], None),
    (["盐路已断，南下潮汐港"], None),
    (["五条南境线，九重命途"], None),
    (["落子无悔，权谋不眠"], "权谋之庭 · TapTap 即刻入局"),
]

## 分镜: (背景构图函数或路径, 时长秒, 运镜方向 in/out/panR, 对应字卡序号 or None)
def img(p):
    return os.path.join(PROJ, p)


def validate_final_card_layout(
    *, main_top, main_bottom, subtitle_top, subtitle_bottom
):
    if main_top < FINAL_CARD_WORDMARK_SAFE_TOP:
        raise ValueError("final card wordmark safe area violated")
    if subtitle_top - main_bottom < FINAL_CARD_MIN_COPY_GAP:
        raise ValueError("final card copy gap is too small")
    if H - subtitle_bottom < FINAL_CARD_BOTTOM_SAFE_MARGIN:
        raise ValueError("final card bottom safe area violated")


def make_card(lines, sub, idx, y_top=None, big_size=None, subtitle_y=None):
    """1920x1080 透明字卡: 大字底部居中 + 羽化暗带(任何底图上可读) + 可选小字。"""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    bsz = big_size or (76 if len(lines) == 1 else 64)
    big = ImageFont.truetype(FONT, bsz, index=0)
    ## 字号自适应: 最长行超过安全宽度(1700px)就逐级缩, 防止长句溢出画面
    _probe = ImageDraw.Draw(Image.new("RGBA", (8, 8)))
    while bsz > 44 and max(_probe.textlength(ln, font=big) for ln in lines) > 1700:
        bsz -= 4
        big = ImageFont.truetype(FONT, bsz, index=0)
    small = ImageFont.truetype(FONT, 34, index=0)
    y = y_top if y_top is not None else H - 300 - (len(lines) - 1) * 88
    ## 羽化暗带: QC 发现潮汐港亮色码头上金字几乎不可见 —— 全宽半透明带 + 高斯羽化,
    ## 使字卡在任何底图上可读
    band_h = len(lines) * 96 + (110 if sub else 30) + 60
    band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(band).rectangle([0, y - 36, W, y - 36 + band_h], fill=(5, 4, 10, 120))
    band = band.filter(ImageFilter.GaussianBlur(22))
    im.alpha_composite(band)
    first_main_top = None
    last_main_bottom = None
    for ln in lines:
        wpx = d.textlength(ln, font=big)
        x = (W - wpx) / 2
        main_box = d.textbbox((x, y), ln, font=big)
        if first_main_top is None:
            first_main_top = main_box[1] - 2
        ## 描边阴影保证任何底图上可读
        for dx, dy in ((2, 2), (-2, 2), (2, -2), (-2, -2), (0, 3)):
            d.text((x + dx, y + dy), ln, font=big, fill=(10, 8, 18, 230))
        d.text((x, y), ln, font=big, fill=(232, 214, 160, 255))
        last_main_bottom = main_box[3] + 3
        y += 96
    if sub:
        wpx = d.textlength(sub, font=small)
        sub_y = subtitle_y if subtitle_y is not None else y + 48
        sub_box = d.textbbox(((W - wpx) / 2, sub_y), sub, font=small)
        if subtitle_y is not None:
            validate_final_card_layout(
                main_top=first_main_top,
                main_bottom=last_main_bottom,
                subtitle_top=sub_box[1],
                subtitle_bottom=sub_box[3],
            )
        divider_y = (
            round((last_main_bottom + sub_box[1]) / 2)
            if subtitle_y is not None
            else y + 26
        )
        d.line([(W / 2 - 140, divider_y), (W / 2 + 140, divider_y)], fill=(212, 169, 66, 180), width=2)
        d.text(((W - wpx) / 2, sub_y), sub, font=small, fill=(200, 184, 144, 255))
    p = os.path.join(WORK, "card%d.png" % idx)
    im.save(p)
    return p


def compose_portraits():
    """深色底 + 四张立绘并排(带脚部渐隐), 供"人物"那一镜。"""
    base = Image.new("RGB", (W, H), (13, 10, 22))
    ## 底部暗角
    vg = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(vg)
    dv.ellipse([-400, -300, W + 400, H + 500], fill=90)
    base.paste(Image.new("RGB", (W, H), (26, 21, 40)), (0, 0), vg)
    xs = [45, 500, 955, 1410]
    for x, name in zip(xs, ["aldric.png", "queen.png", "lily_master.png", "player_char.png"]):
        po = Image.open(img("game/images/" + name)).convert("RGBA")
        po = po.resize((520, int(520 * po.height / po.width)), Image.LANCZOS)
        ## 脚部渐隐蒙版
        m = po.split()[3].point(lambda a: a)
        fade = Image.new("L", po.size, 255)
        df = ImageDraw.Draw(fade)
        for i in range(160):
            df.line([(0, po.height - 160 + i), (po.width, po.height - 160 + i)], fill=255 - int(i * 255 / 160))
        m = Image.composite(Image.new("L", po.size, 0), m, fade.point(lambda a: 255 - a))
        base.paste(po, (x, H - po.height - 60), m)
    p = os.path.join(WORK, "shot_portraits.png")
    base.save(p)
    return p


def compose_tideport():
    """潮汐港背景 + 赛琳立绘右置, 供"外章"那一镜。"""
    bg = Image.open(img("game/images/bg_tideport_harbor.webp")).convert("RGB").resize((W, H), Image.LANCZOS)
    ## 压暗右侧给立绘
    grad = Image.new("L", (W, H), 0)
    dg = ImageDraw.Draw(grad)
    for x in range(W // 2, W):
        dg.line([(x, 0), (x, H)], fill=int((x - W / 2) / (W / 2) * 110))
    bg.paste(Image.new("RGB", (W, H), (8, 8, 14)), (0, 0), grad)
    po = Image.open(img("game/images/corsair.png")).convert("RGBA")
    po = po.resize((640, int(640 * po.height / po.width)), Image.LANCZOS)
    bg.paste(po, (W - 700, H - po.height + 80), po)
    p = os.path.join(WORK, "shot_tideport.png")
    bg.save(p)
    return p


def compose_logo():
    """黑底 logo, 开场镜。"""
    base = Image.new("RGB", (W, H), (6, 5, 10))
    lg = Image.open(img("logo.png")).convert("RGBA")
    lg = lg.resize((1100, int(1100 * lg.height / lg.width)), Image.LANCZOS)
    base.paste(lg, ((W - lg.width) // 2, (H - lg.height) // 2), lg)
    p = os.path.join(WORK, "shot_logo.png")
    base.save(p)
    return p


def compose_cover():
    """收尾镜: 横版主视觉铺满 + 顶部压暗(给两行字卡留空间)。"""
    cv = Image.open(img("cover_horizontal.png")).convert("RGB")
    ratio = max(W / cv.width, H / cv.height)
    cv = cv.resize((int(cv.width * ratio) + 1, int(cv.height * ratio) + 1), Image.LANCZOS)
    cv = cv.crop(((cv.width - W) // 2, (cv.height - H) // 2, (cv.width - W) // 2 + W, (cv.height - H) // 2 + H))
    dk = Image.new("L", (W, H), 0)
    dd = ImageDraw.Draw(dk)
    for y in range(H // 2, H):
        dd.line([(0, y), (W, y)], fill=int((y - H / 2) / (H / 2) * 150))
    cv.paste(Image.new("RGB", (W, H), (8, 6, 14)), (0, 0), dk)
    p = os.path.join(WORK, "shot_cover.png")
    cv.save(p)
    return p


def assert_glyph_coverage():
    """所有字卡文字必须在 FONT 里有字形, 缺一个就拒渲 —— "豺"事故后的硬闸。"""
    from fontTools.ttLib import TTFont
    cmap = TTFont(FONT, fontNumber=0).getBestCmap()
    text = "".join("".join(lines) + (sub or "") for lines, sub in CARDS)
    missing = sorted({c for c in text if ord(c) > 127 and ord(c) not in cmap})
    if missing:
        raise SystemExit("!! 字体缺字形, 拒绝渲染: %r" % missing)


def build():
    assert_glyph_coverage()
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    shots = [
        (compose_logo(), 4.5, "in", None),
        (img("game/images/bg_castle_exterior.webp"), 6.0, "in", 0),
        (img("game/images/bg_throne_room.webp"), 6.0, "panR", 1),
        (compose_portraits(), 6.0, "out", 2),
        (compose_tideport(), 6.0, "in", 3),
        (img("game/images/bg_battlefield_night.webp"), 6.0, "in", 4),
        (compose_cover(), 8.5, "out", 5),
    ]

    segs = []
    for i, (src, dur, mv, card) in enumerate(shots):
        frames = int(dur * FPS)
        ## 防抖: 先放大到 4K 再 zoompan
        if mv == "in":
            zexpr = "zoompan=z='1.001+0.00045*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        elif mv == "out":
            zexpr = "zoompan=z='1.14-0.00045*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        else:  # panR
            zexpr = "zoompan=z=1.12:x='(iw-iw/zoom)*on/%d':y='ih/2-(ih/zoom/2)'" % frames
        zexpr += ":d=%d:s=%dx%d:fps=%d" % (frames, W, H, FPS)
        vf = "[0]scale=2880:1620:force_original_aspect_ratio=increase,crop=2880:1620,%s[b]" % zexpr
        # Feed zoompan one background frame. Looping that input would make its
        # `d=frames` output repeat once per demuxed frame, inflating a short
        # shot into hundreds of seconds.
        inputs = ["-i", src]
        if card is not None:
            ckw = {
                "y_top": FINAL_CARD_MAIN_Y_TOP,
                "big_size": 60,
                "subtitle_y": FINAL_CARD_SUBTITLE_Y,
            } if i == len(shots) - 1 else {}
            cpng = make_card(CARDS[card][0], CARDS[card][1], card, **ckw)
            inputs += [
                "-loop", "1", "-framerate", str(FPS),
                "-t", str(dur), "-i", cpng,
            ]
            vf += ";[1]format=rgba,fade=in:st=0.7:d=0.7:alpha=1,fade=out:st=%.2f:d=0.7:alpha=1[c];[b][c]overlay=format=auto[v]" % (dur - 1.4)
        else:
            vf += ";[b]copy[v]"
        seg = os.path.join(WORK, "seg%d.mp4" % i)
        subprocess.run(["ffmpeg", "-y", "-filter_complex_threads", "4", *inputs,
                        "-filter_complex", vf, "-map", "[v]",
                        "-frames:v", str(frames), "-c:v", "libx264", "-threads", "8",
                        "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", seg],
                       check=True, capture_output=True)
        segs.append((seg, dur))

    ## xfade 串接
    inputs = []
    for s, _ in segs:
        inputs += ["-i", s]
    fc, prev, t = "", "0:v", 0.0
    for i in range(1, len(segs)):
        t += segs[i - 1][1] - XFADE
        nxt = "vx%d" % i
        fc += "[%s][%d:v]xfade=transition=fade:duration=%.2f:offset=%.2f[%s];" % (prev, i, XFADE, t, nxt)
        prev = nxt
    total = t + segs[-1][1]
    ## 配乐: 主题曲, 尾部 2.5s 淡出
    music = img("game/audio/music/main_theme.ogg")
    fc += "[%s]copy[vout]" % prev
    subprocess.run(["ffmpeg", "-y", "-filter_complex_threads", "4", *inputs,
                    "-i", music, "-filter_complex", fc,
                    "-map", "[vout]", "-map", "%d:a" % len(segs),
                    "-af", "afade=out:st=%.2f:d=2.5,volume=0.9" % (total - 2.5),
                    "-t", "%.2f" % total,
                    "-c:v", "libx264", "-threads", "8", "-preset", "medium",
                    "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", OUT], check=True, capture_output=True)
    print("OK ->", OUT, "总时长 %.1fs" % total)


if __name__ == "__main__":
    build()
