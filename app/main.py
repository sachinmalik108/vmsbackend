from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes import streams, summaries, alerts
from fastapi.responses import FileResponse
import os


app = FastAPI()

# CORS (Allow React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app = FastAPI(title="Video Management System")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")

# Mock video data
videos = [
    {"id": 1, "name": "Camera 1", "filename": "cam1.mp4", "status": "active"},
    {"id": 2, "name": "Camera 2", "filename": "cam2.mp4", "status": "active"},
    {"id": 3, "name": "Camera 3", "filename": "cam1.mp4", "status": "active"},
    {"id": 4, "name": "Camera 4", "filename": "cam2.mp4", "status": "active"},
    {"id": 5, "name": "Camera 5", "filename": "cam1.mp4", "status": "active"},
    {"id": 6, "name": "Camera 6", "filename": "cam2.mp4", "status": "active"},
]

@app.get("/api/videos/")
def get_videos():
    return videos


@app.get("/api/videos/{video_id}/stream")
def stream_video(video_id: int):
    video = next((v for v in videos if v["id"] == video_id), None)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")

    video_path = os.path.join(VIDEOS_DIR, video["filename"])
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(video_path, media_type="video/mp4")


app.include_router(streams.router, prefix="/api/streams")
app.include_router(summaries.router, prefix="/api/summaries")
app.include_router(alerts.router, prefix="/api/alerts")

