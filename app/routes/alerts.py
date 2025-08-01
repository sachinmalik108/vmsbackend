from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_alerts():
    return [
                {"stream_id": 1, "alert": "Low confidence in defect detection"},
                {"stream_id": 2, "alert": "High confidence anomaly"},
                {"stream_id": 3, "alert": "Low confidence in defect detection"},
                {"stream_id": 4, "alert": "High confidence anomaly"},
                {"stream_id": 5, "alert": "Low confidence in defect detection"},
                {"stream_id": 6, "alert": "High confidence anomaly"},
                {"stream_id": 7, "alert": "Low confidence in defect detection"},
                {"stream_id": 8, "alert": "High confidence anomaly"},
                {"stream_id": 9, "alert": "Low confidence in defect detection"},
                {"stream_id": 10, "alert": "High confidence anomaly"},


    ]
