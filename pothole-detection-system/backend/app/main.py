import base64
import io
import json
from PIL import UnidentifiedImageError
from app.yolo_inference import detect_potholes_image, detect_potholes_video
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from app.storage import load_stats
from app.storage import get_logs

from app.storage import initialize_stats
initialize_stats()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/logs")
def fetch_logs():
    try:
        return get_logs()
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/stats")
def get_stats():
    stats = load_stats()
    return {
        "image_scanned": stats.get("image_scanned", 0),
        "video_scanned": stats.get("video_scanned", 0),
        "potholes_in_images": stats.get("potholes_in_images", 0),
        "potholes_in_videos": stats.get("potholes_in_videos", 0)
    }


@app.post("/detect")
async def detect_pothole(file: UploadFile = File(...)):
    try:
        content_type = file.content_type
        file_bytes = await file.read()
        print("Received content type:", content_type)

        if content_type in ["image/jpeg", "image/png", "image/jpg"]:
            try:
                results, output_image, pothole_count = detect_potholes_image(file_bytes)
                base64_img = base64.b64encode(output_image).decode("utf-8")
                return {
                    "processed_image": base64_img,
                    "pothole_count": pothole_count
                }
            except UnidentifiedImageError:
                return JSONResponse(status_code=400, content={"error": "Invalid image file."})

        elif content_type in ["video/mp4", "video/mpeg"]:
            output_video, pothole_count = detect_potholes_video(file_bytes)
            return StreamingResponse(io.BytesIO(output_video), media_type="video/mp4",
                                     headers={"x-pothole-count": str(pothole_count)})


        else:
            return JSONResponse(status_code=400, content={"error": f"Unsupported content type: {content_type}"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
