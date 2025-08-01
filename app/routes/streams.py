from fastapi import APIRouter
from app.services.stream_manager import get_active_streams

router = APIRouter()

@router.get("/")
def list_streams():
    return get_active_streams()
