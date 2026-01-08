import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "..", "images")
MAX_FILE_SIZE_MB = 5
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

os.makedirs(IMAGES_DIR, exist_ok=True)