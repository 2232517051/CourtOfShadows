"""Retry failed background images - only the 8 that timed out"""
import requests
import time
import os

API_KEY = "sk-14b51739c53b4e97ba18662a9736f14e"
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'game', 'images')

# Only the 8 that failed
BG_PROMPTS = {
    "bg_castle_exterior": "Medieval stone castle exterior on a hilltop, autumn, grey sky, black mourning banners flying, muddy road leading to gate, oil painting style, dramatic lighting",
    "bg_great_hall": "Medieval great hall interior, large fireplace with roaring fire, golden eagle banner on stone wall, long wooden table, candles, oil painting style, warm lighting",
    "bg_study": "Medieval lord study room, wooden desk covered with scrolls and letters, candle light, bookshelf, fireplace, dark atmosphere, oil painting style",
    "bg_border": "Medieval border outpost, wooden watchtower, soldiers on guard, misty forest background, tense atmosphere, oil painting style, dawn light",
    "bg_council_hall": "Medieval council chamber, round stone table, five ornate chairs, torches on walls, stone arches, political atmosphere, oil painting style",
    "bg_market": "Medieval town marketplace, merchant stalls, cobblestone street, townspeople, half-timbered buildings, lively atmosphere, oil painting style, daytime",
    "bg_forest_path": "Dark medieval forest path at night, moonlight filtering through canopy, mysterious atmosphere, fog, ancient trees, oil painting style",
    "bg_underground": "Medieval underground tunnel, stone walls, torch light, secret passage, ancient carved symbols on walls, mysterious atmosphere, oil painting style",
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
    for _ in range(max_wait // 5):
        time.sleep(5)
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

def download_image(url, filepath):
    resp = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(resp.content)

# Submit 4 at a time to avoid overloading
items = list(BG_PROMPTS.items())
batch_size = 4
success = 0

for batch_start in range(0, len(items), batch_size):
    batch = items[batch_start:batch_start + batch_size]
    tasks = {}

    print(f"\n--- Batch {batch_start // batch_size + 1} ---")
    for name, prompt in batch:
        print(f"Submitting: {name}...")
        task_id = submit_task(prompt)
        if task_id:
            tasks[name] = task_id
            print(f"  Task ID: {task_id}")
        time.sleep(2)

    # Wait for this batch
    for name, task_id in tasks.items():
        print(f"Waiting for: {name}...")
        url = wait_for_task(task_id)
        if url:
            filepath = os.path.join(OUTPUT_DIR, f"{name}.png")
            if os.path.exists(filepath):
                backup = filepath + ".old"
                if not os.path.exists(backup):
                    os.rename(filepath, backup)
                else:
                    os.remove(filepath)
            download_image(url, filepath)
            print(f"  Downloaded!")
            success += 1
        else:
            print(f"  FAILED (timeout)")

print(f"\nDone! {success}/8 images generated.")
