from ultralytics import YOLO
from PIL import Image
from typing import Any

model = YOLO("yolov8n.pt")  

def detect(image: Image.Image, imgsz: int = 640) -> Any:
    """
    Object detection on image 
    """
    results = model(image, imgsz=imgsz)
    return results 
