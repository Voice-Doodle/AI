import os
from datetime import datetime

def generate_unique_filename(original_filename: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename, extension = os.path.splitext(original_filename)
    return f"{filename}_{timestamp}{extension}"
