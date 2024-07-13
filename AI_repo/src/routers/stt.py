from fastapi import APIRouter, UploadFile, File
import whisper
import os
from ..utils import generate_unique_filename

import logging
import time

router = APIRouter(prefix="/stt", tags=["STT"])
model = whisper.load_model("base")

logger = logging.getLogger(__name__)

@router.post("")
async def create_stt_file(audio_file: UploadFile = File(...)) -> str:
    try:
        start_time = time.time()
        logger.info(f"stt 시작")
        file_name = generate_unique_filename(audio_file.filename)
        # 파일을 디스크에 저장
        file_location = f"input/{file_name}"
        with open(file_location, "wb") as file_object:
            file_object.write(await audio_file.read())


        result = model.transcribe(file_location)
        
        os.remove(file_location)
        end_time = time.time()
        logger.info(f"stt 끝 {end_time - start_time}초")
        return result['text']
    except Exception as e:
        return str(e)
