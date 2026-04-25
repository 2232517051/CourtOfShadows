"""批量清理角色立绘背景 - 使用rembg确保完全透明"""
import os
from pathlib import Path
from rembg import remove
from PIL import Image
import io

IMG_DIR = Path(r"C:\Users\22325\Desktop\renpy-8.5.2-sdk\CourtOfShadows\game\images")

# 所有角色PNG（排除bg_开头的背景图）
pngs = sorted([f for f in IMG_DIR.glob("*.png") if not f.name.startswith("bg_")])
print(f"找到 {len(pngs)} 张角色立绘")

for i, png_path in enumerate(pngs, 1):
    print(f"[{i}/{len(pngs)}] 处理 {png_path.name}...", end=" ", flush=True)
    try:
        with open(png_path, "rb") as f:
            input_data = f.read()

        # rembg去背景
        output_data = remove(input_data)

        # 打开处理后的图片，清理半透明像素
        img = Image.open(io.BytesIO(output_data)).convert("RGBA")
        pixels = img.load()
        w, h = img.size

        # 将alpha < 30的像素设为完全透明
        for y in range(h):
            for x in range(w):
                r, g, b, a = pixels[x, y]
                if a < 30:
                    pixels[x, y] = (0, 0, 0, 0)

        img.save(png_path, "PNG")
        print("OK")
    except Exception as e:
        print(f"ERROR: {e}")

print("\n全部完成！")
