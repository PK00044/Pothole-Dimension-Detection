import json
from pathlib import Path
from datetime import datetime

# File paths
STATS_FILE = Path("Storage/detection_stats.json")
LOG_FILE = Path("Storage/detection_logs.json")


def initialize_stats():
    STATS_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not STATS_FILE.exists():
        default_stats = {
            "image_count": 0,
            "video_count": 0,
            "image_potholes": 0,
            "video_potholes": 0
        }
        with open(STATS_FILE, "w") as f:
            json.dump(default_stats, f, indent=4)

    # Initialize logs file
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)


def load_stats():
    with open(STATS_FILE, "r") as f:
        return json.load(f)


def update_stats(key, increment=1):
    stats = load_stats()
    stats[key] = stats.get(key, 0) + increment
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def update_pothole_count(key, count):
    stats = load_stats()
    stats[key] = stats.get(key, 0) + count
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def log_detection(file_type: str, potholes: int):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "file_type": file_type,
        "potholes_detected": potholes
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def get_logs():
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

