"""Regenerate background images in 1280x720 (16:9) using DashScope wanx API"""
import requests
import time
import os

API_KEY = "sk-14b51739c53b4e97ba18662a9736f14e"
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'game', 'images')

# Background image prompts - oil painting medieval style, 16:9 ratio
BG_PROMPTS = {
    "bg_castle_exterior": "Medieval stone castle exterior on a hilltop, autumn, grey sky, black mourning banners flying, muddy road leading to gate, oil painting style, dramatic lighting, 16:9 aspect ratio",
    "bg_great_hall": "Medieval great hall interior, large fireplace with roaring fire, golden eagle banner on stone wall, long wooden table, candles, oil painting style, warm lighting, 16:9",
    "bg_study": "Medieval lord's study room, wooden desk covered with scrolls and letters, candle light, bookshelf, fireplace, dark atmosphere, oil painting style, 16:9",
    "bg_border": "Medieval border outpost, wooden watchtower, soldiers on guard, misty forest background, tense atmosphere, oil painting style, dawn light, 16:9",
    "bg_council_hall": "Medieval council chamber, round stone table, five ornate chairs, torches on walls, stone arches, political atmosphere, oil painting style, 16:9",
    "bg_market": "Medieval town marketplace, merchant stalls, cobblestone street, townspeople, half-timbered buildings, lively atmosphere, oil painting style, daytime, 16:9",
    "bg_forest_path": "Dark medieval forest path at night, moonlight filtering through canopy, mysterious atmosphere, fog, ancient trees, oil painting style, 16:9",
    "bg_underground": "Medieval underground tunnel, stone walls, torch light, secret passage, ancient carved symbols on walls, mysterious atmosphere, oil painting style, 16:9",
    "bg_church_interior": "Medieval Gothic church interior, stained glass windows, altar with candles, stone pillars, religious atmosphere, golden light rays, oil painting style, 16:9",
    "bg_royal_palace": "Grand medieval royal palace exterior, marble columns, golden decorations, guards at entrance, imposing architecture, oil painting style, sunset, 16:9",
    "bg_throne_room": "Medieval throne room, ornate golden throne on elevated platform, red carpet, courtiers standing, crown insignia, oil painting style, majestic lighting, 16:9",
    "bg_palace_garden": "Medieval palace garden at night, moonlit rose bushes, stone fountain, marble benches, romantic atmosphere, oil painting style, 16:9",
    "bg_dungeon": "Medieval dungeon, iron bars, chains on stone walls, single torch, dark and damp, rats, oppressive atmosphere, oil painting style, 16:9",
    "bg_battlefield": "Medieval battlefield aftermath, banners in wind, swords stuck in ground, dramatic clouds, epic atmosphere, oil painting style, golden hour lighting, 16:9",
}

def submit_task(prompt, size="1280*720"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }
    data = {
        "model": "wanx-v1",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": size,
            "n": 1,
            "style": "<oil painting>"
        }
    }
    resp = requests.post(BASE_URL, headers=headers, json=data)
    result = resp.json()
    if "output" in result and "task_id" in result["output"]:
        return result["output"]["task_id"]
    else:
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
    print(f"  Timeout waiting for task {task_id}")
    return None

def download_image(url, filepath):
    resp = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(resp.content)

def main():
    print(f"Generating {len(BG_PROMPTS)} background images in 1280x720...")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Submit all tasks first
    tasks = {}
    for name, prompt in BG_PROMPTS.items():
        print(f"Submitting: {name}...")
        task_id = submit_task(prompt)
        if task_id:
            tasks[name] = task_id
            print(f"  Task ID: {task_id}")
        else:
            print(f"  FAILED to submit")
        time.sleep(1)  # rate limiting

    print(f"\n{len(tasks)} tasks submitted. Waiting for results...\n")

    # Wait for all tasks
    success = 0
    for name, task_id in tasks.items():
        print(f"Waiting for: {name}...")
        url = wait_for_task(task_id)
        if url:
            filepath = os.path.join(OUTPUT_DIR, f"{name}.png")
            # Backup old image
            if os.path.exists(filepath):
                backup = filepath + ".old"
                if not os.path.exists(backup):
                    os.rename(filepath, backup)
                else:
                    os.remove(filepath)
            download_image(url, filepath)
            print(f"  Downloaded: {filepath}")
            success += 1
        else:
            print(f"  FAILED")

    print(f"\nDone! {success}/{len(tasks)} images generated successfully.")

if __name__ == "__main__":
    main()
