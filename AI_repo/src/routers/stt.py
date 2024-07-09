from fastapi import APIRouter, UploadFile, File
import whisper
import os
from ..utils import generate_unique_filename

router = APIRouter(prefix="/stt", tags=["STT"])
model = whisper.load_model("base")

@router.post("")
async def create_stt_file(audio_file: UploadFile = File(...)) -> str:
    try:
        file_name = generate_unique_filename(audio_file.filename)
        # 파일을 디스크에 저장
        file_location = f"input/{file_name}"
        with open(file_location, "wb") as file_object:
            file_object.write(await audio_file.read())


        result = model.transcribe(file_location)
        
        os.remove(file_location)

        return result['text']
    except Exception as e:
        return str(e)
