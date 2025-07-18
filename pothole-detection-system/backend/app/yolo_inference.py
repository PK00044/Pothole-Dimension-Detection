import tempfile
from io import BytesIO

import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from app.storage import log_detection
import os
import json
from datetime import datetime

ARCHIVE_DIR = "Storage/archives"
os.makedirs(ARCHIVE_DIR, exist_ok=True)

from app.storage import update_stats, update_pothole_count, log_detection

# Load model
model = YOLO("../model/best.pt")

# Global statistics counters
image_count = 0
video_count = 0
image_potholes = 0
video_potholes = 0


def detect_potholes_image(image_bytes: bytes):
    global image_count, image_potholes

    image_count += 1  # Count this image scan

    # Convert bytes to image
    image_pil = Image.open(BytesIO(image_bytes)).convert("RGB")
    image_cv = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    # Run YOLOv8 detection
    results = model(image_pil)
    pixel_to_meter = 1 / 320  # Assuming 320 pixels ≈ 1 meter

    pothole_count = 0

    for r in results:
        for box in r.boxes:
            pothole_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            width = (x2 - x1) * pixel_to_meter
            height = (y2 - y1) * pixel_to_meter
            label = f"{width:.2f}m x {height:.2f}m"
            cv2.rectangle(image_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image_cv, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    update_stats("image_scanned")
    log_detection("image", pothole_count)

    update_pothole_count("potholes_in_images", len(results[0].boxes))

    image_potholes += pothole_count

    # Convert result back to JPEG
    result_pil = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
    buf = BytesIO()
    result_pil.save(buf, format="JPEG")

    return results, buf.getvalue(), pothole_count


def detect_potholes_video(video_bytes: bytes):
    global video_count, video_potholes

    video_count += 1

    # Save uploaded video to temp file
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(video_bytes)
    temp_input.close()

    cap = cv2.VideoCapture(temp_input.name)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")

    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(temp_output.name, fourcc, fps, (w, h))

    pothole_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for r in results:
            for box in r.boxes:
                pothole_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                width = (x2 - x1) / 320
                height = (y2 - y1) / 320
                label = f"{width:.2f}m x {height:.2f}m"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    update_stats("video_scanned")
    log_detection("video", pothole_count)
    update_pothole_count("potholes_in_videos", pothole_count)

    with open(temp_output.name, "rb") as f:
        video_bytes = f.read()

    video_potholes += pothole_count
    return video_bytes, pothole_count
