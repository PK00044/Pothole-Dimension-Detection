import cv2
import numpy as np
from ultralytics import YOLO
import streamlit as st

model = YOLO("backend/model/best2.pt")


def run_realtime(camera_source):
    cap = cv2.VideoCapture(camera_source)

    if not cap.isOpened():
        st.error("❌ Unable to open camera.")
        return

    stframe = st.empty()
    pixel_to_meter = 1 / 320

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                width = (x2 - x1) * pixel_to_meter
                height = (y2 - y1) * pixel_to_meter
                label = f"{width:.2f}m x {height:.2f}m"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Convert to RGB and display
        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")

    cap.release()
