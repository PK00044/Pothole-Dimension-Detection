# 🕳️ Real-Time Pothole Detection System

A machine learning-powered pothole detection solution capable of identifying potholes in **images**, **videos**, and **live streams** using **YOLOv8**. It estimates pothole dimensions and provides real-time visual feedback, all through a user-friendly interface built with **Streamlit** and a backend powered by **FastAPI**.

---

## 📌 Features

* 🖼️ Image and video-based pothole detection
* 🔴 Real-time detection via PC webcam or mobile camera (DroidCam)
* 📏 Pothole dimension estimation (width × height in meters)
* 📊 Interactive dashboard with:

  * Total images/videos scanned
  * Potholes detected
  * Date-wise detection charts
  * Recent upload history
  * CSV/JSON export functionality
* 📁 Media preview and download support (for both image and video)

---

## ⚙️ Tech Stack

| Layer    | Tools/Technologies             |
| -------- | ------------------------------ |
| Frontend | Streamlit                      |
| Backend  | FastAPI                        |
| ML Model | YOLOv8 (`ultralytics` library) |
| Language | Python                         |
| Charts   | Plotly, pandas                 |
| Storage  | JSON (for logs and stats)      |

---

## 📂 Project Structure

```
pothole-detection-system/
│
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI server
│   │   ├── yolo_inference.py       # YOLOv8 detection functions
│   │   ├── storage.py              # Stats & log handling
│   │   └── model/                  # best.pt (YOLOv8 model)
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py            # Entry point (or run with `streamlit run`)
│   ├── home.py                     # Home page
│   ├── image_video.py             # Image/Video detection page
│   ├── realtime.py                # Real-time detection page
│   └── dashboard.py               # Dashboard and stats
│
├── Storage/
│   ├── detection_stats.json        # Stats storage
│   └── detection_logs.json         # Logs storage
│
├── home.md                         # Markdown file for homepage content
└── README.md
```

---

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pothole-detection-system.git
cd pothole-detection-system
```

### 2. Install dependencies

For both backend and frontend:

```bash
pip install -r backend/requirements.txt
```

**Additional tools:**

* `ultralytics`: for YOLOv8 model
* `opencv-python`, `Pillow`, `requests`, `streamlit`, `fastapi`, `uvicorn`, `plotly`, `pandas`

### 3. Download the YOLOv8 model

Place your trained YOLOv8 model in:

```
backend/app/model/best.pt
```

### 4. Start FastAPI backend

```bash
cd backend
uvicorn app.main:app --reload
```

### 5. Start Streamlit frontend

```bash
cd frontend
streamlit run home.py
```

---

## 🔍 Sample Usage

* **Home**: Introduction and usage guide.
* **Image/Video Detection**: Upload media and get detected results.
* **Real-time Detection**: Start detection with your webcam or DroidCam mobile feed.
* **Dashboard**: View logs, stats, trends, and download session summaries.

---

## 📈 Dashboard Snapshot

* 📅 Date-wise pothole detection trends
* 🖼️ Images vs 🎞️ videos processed
* 📊 Daily detection bar chart
* 💾 Download CSV or JSON logs

---

## 📦 Future Work

* Integration with GPS to mark pothole locations on a map
* Notification alerts 100m before potholes (via coordinates)
* Admin panel for road maintenance agencies
* Heatmap generation and risk-level categorization
* Multilingual and voice-enabled interface


