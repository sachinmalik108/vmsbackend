import random

def simulate_asset_detection(stream_id: int):
    return {"stream_id": stream_id, "summaryText": "Asset detected", "confidence": random.uniform(0.6, 0.95)}

def simulate_defect_detection(stream_id: int):
    return {"stream_id": stream_id, "summaryText": "No defect", "confidence": random.uniform(0.7, 0.99)}
