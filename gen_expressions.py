"""Generate character expression variants using DashScope wanx API.
Each character gets 4 expressions: normal (existing), angry, sad, happy.
Output as WebP to game/images/ directory."""
import requests
import time
import os
from PIL import Image
import io

API_KEY = "sk-14b51739c53b4e97ba18662a9736f14e"
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'game', 'images')

# Character base descriptions + expression modifiers
CHARACTERS = {
    "aldric": "An old medieval knight with grey hair and beard, loyal face, wearing plate armor, dark red cloak, portrait style, oil painting, dark background",
    "elena": "A beautiful young medieval woman with mysterious purple eyes, dark hair, wearing elegant purple dress, court emissary, portrait style, oil painting, dark background",
    "bishop": "A middle-aged medieval bishop in golden religious robes, wise face, holding a staff, religious authority, portrait style, oil painting, dark background",
    "baron": "A stern middle-aged medieval nobleman with sharp features, dark green cloak, ambitious expression, wealthy lord, portrait style, oil painting, dark background",
    "captain": "A young medieval military captain with a scar across his nose, wearing steel blue armor, strong jaw, soldier, portrait style, oil painting, dark background",
    "queen": "A regal medieval queen in her 40s, purple royal dress, crown, powerful and intelligent expression, portrait style, oil painting, dark background",
    "prince": "A young handsome medieval prince with royal blue cloak, idealistic expression, golden crown, portrait style, oil painting, dark background",
    "merchant_karl": "A shrewd medieval merchant in brown clothing, calculating eyes, rings on fingers, wealthy trader, portrait style, oil painting, dark background",
    "lily_master": "A mysterious figure in dark purple hooded cloak, shadowy face, secret organization leader, enigmatic, portrait style, oil painting, dark background",
}

EXPRESSIONS = {
    "angry": ", angry expression, furrowed brows, intense eyes, clenched jaw",
    "sad": ", sad expression, downcast eyes, melancholy look, sorrowful",
    "happy": ", happy expression, gentle smile, warm eyes, pleased look",
}


def submit_task(prompt, size="1024*1024"):
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
    total = len(CHARACTERS) * len(EXPRESSIONS)
    print(f"Generating {total} expression images for {len(CHARACTERS)} characters...")
    print(f"Expressions: {list(EXPRESSIONS.keys())}")
    print(f"Output: {OUTPUT_DIR}\n")

    # Submit all tasks
    tasks = {}
    for char_name, base_prompt in CHARACTERS.items():
        for expr_name, expr_modifier in EXPRESSIONS.items():
            key = f"{char_name}_{expr_name}"
            filepath = os.path.join(OUTPUT_DIR, f"{key}.webp")
            if os.path.exists(filepath):
                print(f"Skipping {key} (already exists)")
                continue
            prompt = base_prompt + expr_modifier
            print(f"Submitting: {key}...")
            task_id = submit_task(prompt)
            if task_id:
                tasks[key] = task_id
                print(f"  Task ID: {task_id}")
            time.sleep(1)

    if not tasks:
        print("All expression images already exist!")
        return

    print(f"\n{len(tasks)} tasks submitted. Waiting for results...\n")

    success = 0
    for key, task_id in tasks.items():
        print(f"Waiting: {key}...")
        url = wait_for_task(task_id)
        if url:
            filepath = os.path.join(OUTPUT_DIR, f"{key}.webp")
            download_as_webp(url, filepath)
            success += 1
        else:
            print(f"  FAILED")

    print(f"\nDone! {success}/{len(tasks)} expression images generated.")


if __name__ == "__main__":
    main()
