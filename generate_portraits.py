"""
角色立绘生成脚本 - 使用通义万相 (Wanx) API
运行: python generate_portraits.py
生成结果保存到 game/images/ 目录
"""

import os
import sys
import time
import requests
from dashscope import ImageSynthesis

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

API_KEY = "sk-14b51739c53b4e97ba18662a9736f14e"

# 输出目录
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "game", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 通用风格前缀
STYLE = (
    "medieval fantasy character portrait, oil painting style, "
    "detailed face, dramatic lighting, dark castle background, "
    "high quality, 4k, masterpiece"
)

# 角色定义：文件名 -> 英文提示词
CHARACTERS = {
    "aldric": (
        f"{STYLE}, elderly man in his 70s, white hair and beard, "
        "wise eyes, wearing dark steward robes with silver chain, "
        "holding a candle, loyal but secretive expression, "
        "wrinkled face showing years of service"
    ),
    "elena": (
        f"{STYLE}, young woman in her 20s, dark brown hair in braids, "
        "sharp intelligent eyes, wearing simple but elegant purple dress, "
        "subtle mysterious smile, court spy and handmaiden, "
        "beautiful but dangerous aura"
    ),
    "bishop": (
        f"{STYLE}, middle-aged man in his 50s, bald head, "
        "wearing golden bishop robes and mitre, holding a staff, "
        "ambitious cunning expression, religious authority, "
        "candlelight reflecting off golden vestments"
    ),
    "baron": (
        f"{STYLE}, muscular man in his 40s, dark beard, scarred face, "
        "wearing dark iron armor with fur cloak, stern threatening gaze, "
        "military commander, medieval warlord aesthetic, "
        "standing before army banners"
    ),
    "captain": (
        f"{STYLE}, strong man in his 30s, short brown hair, "
        "wearing chain mail and blue tabard with eagle emblem, "
        "honest straightforward expression, hand on sword hilt, "
        "loyal knight and guard captain"
    ),
    "queen": (
        f"{STYLE}, regal woman in her 40s, silver crown, "
        "long black hair, wearing royal purple gown with gold embroidery, "
        "cold authoritative gaze, iron-willed ruler, "
        "sitting on throne, majestic and intimidating"
    ),
}

# 场景背景
SCENES = {
    "bg_castle_exterior": (
        "medieval castle on a hilltop, rainy autumn day, "
        "black mourning flags, muddy road, grey sky, "
        "oil painting style, wide landscape, atmospheric, 4k"
    ),
    "bg_great_hall": (
        "medieval castle great hall interior, large fireplace burning, "
        "golden eagle banner on stone wall, wooden long table, "
        "candle chandeliers, warm lighting, oil painting, 4k"
    ),
    "bg_study": (
        "medieval lord's study room at night, desk with parchments and candles, "
        "bookshelf, fireplace, dark atmospheric, single candle light, "
        "oil painting style, 4k"
    ),
    "bg_border": (
        "medieval army camp at border, soldiers and tents, "
        "misty hills background, war banners, autumn landscape, "
        "wide shot, oil painting style, dramatic sky, 4k"
    ),
}


def generate_image(name: str, prompt: str):
    """调用通义万相生成图片并保存"""
    print(f"\n🎨 正在生成: {name}")
    print(f"   提示词: {prompt[:80]}...")

    try:
        task = ImageSynthesis.call(
            model="wanx-v1",
            prompt=prompt,
            n=1,
            size="1024*1024",
            api_key=API_KEY,
        )

        if task.status_code == 200:
            url = task.output.results[0].url
            print(f"   ✅ 生成成功: {url}")

            # 下载图片
            resp = requests.get(url, timeout=60)
            filepath = os.path.join(OUTPUT_DIR, f"{name}.png")
            with open(filepath, "wb") as f:
                f.write(resp.content)
            print(f"   💾 已保存: {filepath}")
            return True
        else:
            print(f"   ❌ 失败 ({task.status_code}): {task.message}")
            return False

    except Exception as e:
        print(f"   ❌ 异常: {e}")
        return False


def main():
    print("=" * 60)
    print("  权谋之庭 - 角色立绘 & 场景背景 生成器")
    print("=" * 60)

    total = len(CHARACTERS) + len(SCENES)
    success = 0

    print(f"\n📋 共 {len(CHARACTERS)} 个角色 + {len(SCENES)} 个场景 = {total} 张图")
    print(f"📂 输出目录: {OUTPUT_DIR}\n")

    # 生成角色立绘
    print("--- 角色立绘 ---")
    for name, prompt in CHARACTERS.items():
        if generate_image(name, prompt):
            success += 1
        time.sleep(2)  # 避免请求过快

    # 生成场景背景
    print("\n--- 场景背景 ---")
    for name, prompt in SCENES.items():
        if generate_image(name, prompt):
            success += 1
        time.sleep(2)

    print(f"\n{'=' * 60}")
    print(f"  完成！成功 {success}/{total} 张")
    print(f"  图片保存在: {OUTPUT_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
