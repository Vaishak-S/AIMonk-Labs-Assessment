import os
from typing import Any
from PIL import Image
import json

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_image(image: Image.Image, path: str):
    image.save(path)

def to_json(data: Any) -> str:
    return json.dumps(data, indent=4)

def from_json(json_str: str) -> Any:
    return json.loads(json_str)
