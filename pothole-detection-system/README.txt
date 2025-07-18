Pothole Dimension Detection System – README

1. Project Overview
This project implements a YOLOv8-based pothole detection and dimension estimation system capable of processing images, videos, and real-time camera input (PC & mobile via DroidCam). The software includes:
- Object detection using YOLOv8
- Dimension overlay in meters
- Streamlit frontend with UI for image/video upload
- Real-time detection sidebar
- GPS and notification modules (planned)

2.  Software & Hardware Requirements
 Software Requirements
- Python 3.10 or later
- OS: Windows 10 / Linux / macOS
- Required Python packages (see requirements.txt):
  - ultralytics
  - streamlit
  - opencv-python
  - numpy
  - requests
  - pillow
  - fastapi
  - uvicorn
  - pyngrok (for external access via ngrok)

Hardware Requirements
- Minimum 4GB RAM, recommended 8GB+
- GPU (optional but recommended for faster YOLO inference)
- Webcam for real-time detection

3. File Structure

pothole-detection-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI backend
│   │   ├── yolo_inference.py      # Detection logic
│   │   └── realtime_detector.py   # Realtime detection module
│
├── model/
│   └── best.pt                    # Trained YOLOv8 model weights
│
├── streamlit_app.py              # Streamlit frontend
├── requirements.txt              # All dependencies
├── README.txt                    # This file

4. Salient Features

- Detects potholes in static images and videos
- Estimates width and height in meters
- Streamlit-based user-friendly UI
- Realtime detection using webcam or mobile camera
- Works offline (local FastAPI + YOLOv8 model)
- Extensible to include GPS mapping, voice alerts, and notifications

5. How to Run

Backend Setup
1. Open terminal in backend/app/
2. Run the FastAPI server:
   uvicorn main:app --reload --port 8000

Frontend Setup
1. In project root:
   streamlit run streamlit_app.py

2. Open http://localhost:8501/ in browser.

6. Compiling/Running Procedure
No compilation needed. Python interpreted code.

Ensure requirements.txt is installed:
pip install -r requirements.txt

7. Public Domain Acknowledgments

This project uses the following open-source resources:

- Ultralytics YOLOv8
  - Site: https://github.com/ultralytics/ultralytics
  - License: GPL-3.0
  - Module used: ultralytics.yolo

- Flickr Pothole Dataset (or Roboflow if used)
  - Dataset URL: https://universe.roboflow.com
  - License: CC BY 4.0
