"""
中世纪BGM下载脚本
从免费音乐资源下载适合中世纪题材的背景音乐

所有音乐来自 Pixabay (免费商用授权)
运行: python download_music.py
"""

import os
import requests

MUSIC_DIR = os.path.join(os.path.dirname(__file__), "game", "audio", "music")
SFX_DIR = os.path.join(os.path.dirname(__file__), "game", "audio", "sfx")
os.makedirs(MUSIC_DIR, exist_ok=True)
os.makedirs(SFX_DIR, exist_ok=True)

# Pixabay 免费音乐 (CC0 / Pixabay License)
# 注意：Pixabay 的直接下载链接需要登录，以下提供搜索指引
MUSIC_SOURCES = """
====================================================
  中世纪 BGM 资源指南
====================================================

推荐从以下网站下载免费中世纪风格音乐：

1. Pixabay Music (免费商用, 无需署名)
   https://pixabay.com/music/search/medieval/
   推荐搜索关键词：medieval, celtic, fantasy, castle

2. OpenGameArt (CC0/CC-BY)
   https://opengameart.org/art-search-advanced?keys=medieval&type=music
   大量游戏专用中世纪音乐

3. FreePD (公共领域)
   https://freepd.com/
   搜索 Epic / Fantasy 分类

4. Incompetech (Kevin MacLeod, CC-BY)
   https://incompetech.com/music/royalty-free/music.html
   搜索: Medieval, Renaissance, Fantasy

推荐下载的音乐类型和对应场景：

  文件名                    用途              推荐风格
  ─────────────────────────────────────────────────────
  main_theme.ogg           主菜单            史诗管弦乐
  castle_calm.ogg          城堡日常          竖琴+鲁特琴
  great_hall.ogg           大厅场景          庄严管弦乐
  tension.ogg              紧张/阴谋         低沉弦乐
  battle_prepare.ogg       备战/对峙         鼓点+号角
  night_mystery.ogg        夜晚/密谈         神秘氛围
  victory.ogg              胜利/成就         凯旋进行曲
  sad.ogg                  悲伤/丧礼         缓慢弦乐

  下载后请转换为 .ogg 格式放入:
  game/audio/music/

音效（放入 game/audio/sfx/）：
  door_knock.ogg           敲门声
  sword_draw.ogg           拔剑
  fire_crackle.ogg         壁炉噼啪
  horse_gallop.ogg         马蹄声
  crowd_murmur.ogg         人群低语
  bell_toll.ogg            钟声

====================================================
"""


def create_placeholder_files():
    """创建占位音频文件（提示用户替换）"""
    music_files = [
        "main_theme.ogg",
        "castle_calm.ogg",
        "great_hall.ogg",
        "tension.ogg",
        "battle_prepare.ogg",
        "night_mystery.ogg",
        "victory.ogg",
        "sad.ogg",
    ]

    sfx_files = [
        "door_knock.ogg",
        "sword_draw.ogg",
        "fire_crackle.ogg",
        "horse_gallop.ogg",
        "crowd_murmur.ogg",
        "bell_toll.ogg",
    ]

    print("📂 创建音乐目录占位文件...\n")

    for f in music_files:
        path = os.path.join(MUSIC_DIR, f"{f}.txt")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(f"请将 {f} 音频文件放在此目录下，并删除此 .txt 文件\n")
        print(f"  📄 music/{f}.txt (占位)")

    for f in sfx_files:
        path = os.path.join(SFX_DIR, f"{f}.txt")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(f"请将 {f} 音效文件放在此目录下，并删除此 .txt 文件\n")
        print(f"  📄 sfx/{f}.txt (占位)")


def main():
    print(MUSIC_SOURCES)
    create_placeholder_files()

    print(f"\n✅ 目录结构已创建:")
    print(f"   {MUSIC_DIR}")
    print(f"   {SFX_DIR}")
    print(f"\n💡 下载音乐后放入对应目录，Ren'Py 即可自动识别。")
    print(f"   推荐格式: .ogg (最佳兼容性) 或 .mp3")


if __name__ == "__main__":
    main()
