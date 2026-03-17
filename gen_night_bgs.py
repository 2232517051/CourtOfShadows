"""Generate night/dusk variants of outdoor background images using DashScope wanx API.
Only generates for outdoor scenes that make sense with time-of-day changes."""
import requests
import time
import os
from PIL import Image
import io

API_KEY = "sk-14b51739c53b4e97ba18662a9736f14e"
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'game', 'images')

# Only outdoor/semi-outdoor scenes that benefit from night variants
NIGHT_BG_PROMPTS = {
    "bg_castle_exterior_night": "Medieval stone castle exterior on a hilltop at night, moonlight, stars, torches on walls, dark blue sky, oil painting style, dramatic moonlit lighting, 16:9 aspect ratio",
    "bg_border_night": "Medieval border outpost at night, watchtower with torchlight, soldiers on night watch, starry sky, campfires, tense atmosphere, oil painting style, 16:9",
    "bg_market_night": "Medieval town marketplace at night, empty stalls, cobblestone street, moonlight, few lanterns, quiet atmosphere, oil painting style, 16:9",
    "bg_battlefield_night": "Medieval battlefield at night, moonlit field, banners in wind, fires burning, dramatic clouds, aftermath, oil painting style, 16:9",
    "bg_royal_palace_night": "Grand medieval royal palace exterior at night, moonlit marble columns, torches at entrance, guards, starry sky, oil painting style, 16:9",
}

# Dusk/sunset variants for atmosphere
DUSK_BG_PROMPTS = {
    "bg_castle_exterior_dusk": "Medieval stone castle exterior on a hilltop at sunset, orange and purple sky, dramatic clouds, warm golden light, oil painting style, 16:9 aspect ratio",
    "bg_border_dusk": "Medieval border outpost at dusk, sunset sky, soldiers ending shift, warm orange lighting, oil painting style, 16:9",
    "bg_palace_garden_dusk": "Medieval palace garden at dusk, sunset light on rose bushes, golden hour, warm atmosphere, oil painting style, 16:9",
}


def submit_task(prompt, size="1280*720"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }
    data = {
        "model": "wanx-v1",
        "input": {"prompt": prompt},
        "parameters": {"size": size, "n": 1, "style": "<oil painting>"}
    }
    resp = requests.post(BASE_URL, headers=headers, json=data)
    result = resp.json()
    if "output" in result and "task_id" in result["output"]:
        return result["output"]["task_id"]
    print(f"  Error: {result}")
    return None


def wait_for_task(task_id, max_wait=300):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    for _ in range(max_wait // 3):
        time.sleep(3)
        resp = requests.get(url, headers=headers)
        result = resp.json()
        status = result.get("output", {}).get("task_status", "")
        if status == "SUCCEEDED":
            results = result["output"].get("results", [])
            if results:
                return results[0].get("url")
        elif status == "FAILED":
            print(f"  Task failed: {result}")
            return None
    return None


def download_as_webp(url, filepath):
    resp = requests.get(url)
    img = Image.open(io.BytesIO(resp.content))
    img.save(filepath, 'WEBP', quality=85)
    print(f"  Saved: {filepath} ({os.path.getsize(filepath) // 1024}KB)")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_prompts = {**NIGHT_BG_PROMPTS, **DUSK_BG_PROMPTS}
    print(f"Generating {len(all_prompts)} time-of-day background variants...")
    print(f"Output: {OUTPUT_DIR}\n")

    tasks = {}
    for name, prompt in all_prompts.items():
        filepath = os.path.join(OUTPUT_DIR, f"{name}.webp")
        if os.path.exists(filepath):
            print(f"Skipping {name} (already exists)")
            continue
        print(f"Submitting: {name}...")
        task_id = submit_task(prompt)
        if task_id:
            tasks[name] = task_id
            print(f"  Task ID: {task_id}")
        time.sleep(1)

    if not tasks:
        print("All background variants already exist!")
        return

    print(f"\n{len(tasks)} tasks submitted. Waiting for results...\n")

    success = 0
    for name, task_id in tasks.items():
        print(f"Waiting: {name}...")
        url = wait_for_task(task_id)
        if url:
            filepath = os.path.join(OUTPUT_DIR, f"{name}.webp")
            download_as_webp(url, filepath)
            success += 1
        else:
            print(f"  FAILED")

    print(f"\nDone! {success}/{len(tasks)} background variants generated.")


if __name__ == "__main__":
    main()
