from fastapi import APIRouter
from app.models.ai_models import simulate_asset_detection, simulate_defect_detection

router = APIRouter()

@router.get("/")
def get_model_summaries():
    return [
        simulate_asset_detection(1),
        simulate_defect_detection(1),
        simulate_asset_detection(2),
        simulate_defect_detection(2),
        simulate_asset_detection(3),
        simulate_defect_detection(3),
        simulate_asset_detection(4),
        simulate_defect_detection(4),
        simulate_asset_detection(5),
        simulate_defect_detection(5),
        simulate_asset_detection(6),
        simulate_defect_detection(6),
        simulate_asset_detection(7),
    ]
