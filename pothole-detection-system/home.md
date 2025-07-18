

Welcome to our **Pothole Dimension Detection Application**, a deep learning-based road safety solution powered by **YOLOv8**, designed to accurately detect potholes and estimate their dimensions in real-time. This application enables users to analyze road conditions through image, video, and live webcam inputs, enhancing both road maintenance planning and public safety.

This project is developed as part of the **VTU Major Project 2025**.

---

## 🧠 Powered by YOLOv8 (You Only Look Once Version 8)

Our detection model is built using **YOLOv8**, one of the most advanced real-time object detection algorithms. YOLOv8 is known for its:

- Fast and accurate detection
- Lightweight architecture for real-time deployment
- Support for bounding box regression and instance segmentation
- Built-in model export options (ONNX, TensorRT, CoreML)

We fine-tuned the model on a custom dataset of annotated pothole images collected from **Indian road conditions** using Roboflow and real-world captures. The model can detect potholes and overlay their **width and height in meters** using pixel-to-meter conversion logic.
![YOLOv8 Architecture](assets/yolo_diagram.png)
---

## 🛠️ How YOLOv8 Works in This Project

1. **Input**: Accepts image, video, or live webcam feed (mobile or PC camera).
2. **Preprocessing**: The input frame is resized and normalized to fit the model input size (640x640 by default).
3. **Detection**: YOLOv8 processes the frame, identifies potholes, and generates bounding boxes.
4. **Dimension Estimation**: Bounding box coordinates are converted into real-world dimensions using a pixel-to-meter conversion ratio (e.g., 1 pixel ≈ 1/320 m).
5. **Visualization**: Output frames display bounding boxes with width × height labels.
6. **Post-processing**: Results can be previewed, saved, or downloaded for reporting and analysis.

![Detailed Flowchart](assets/detailed_flowchart.png)
---

## 📦 Key Features

- 🔍 **Pothole Detection** using YOLOv8 trained on custom datasets
- 📏 **Dimension Estimation** (in meters) for each detected pothole
- 🖼️ **Supports Image, Video, and Real-Time Camera Input**
- 📍 **Future Plans**: Add GPS tagging, early warning alerts, and cloud-based damage mapping
![Flowchart](assets/flowchart.png)
---

## 📁 Try the Apps Using Sidebar

Use the **sidebar menu** to explore various interfaces of our detection system:
- **Upload Image**: Detect potholes from a photo
- **Upload Video**: Process and detect potholes in recorded videos
- **Real-Time Detection**: Use your PC or mobile camera for live pothole detection (via DroidCam/Webcam)
- **Result Previews**: View annotated frames and dimension overlays

---

## 📊 Application Goals

- Improve municipal road maintenance by automating pothole logging
- Provide live pothole detection in vehicles for early warnings
- Assist smart cities with AI-based road infrastructure analysis
