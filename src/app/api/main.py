import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from app.models.yolo import detect 
from app.utils.file_utils import ensure_dir, save_image

# Directories
UPLOAD_DIR = "uploaded_images"
OUTPUT_DIR = "outputs"

ensure_dir(UPLOAD_DIR)
ensure_dir(OUTPUT_DIR)

app = FastAPI(title="YOLOv8 Object Detection API")

@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    try:
        # Read and save uploaded image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # Object detection
        results = detect(image, imgsz=640)
        detections = results[0].to_json()  

        # Build response
        response = {
            "detections": detections
        }
        return JSONResponse(content=response, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
