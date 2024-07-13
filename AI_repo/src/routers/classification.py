from fastapi import APIRouter
import whisper
import os
from transformers import pipeline

import logging
import time

router = APIRouter(prefix="/classification", tags=["Classification"])
zeroshot_classifier = pipeline("zero-shot-classification", model="MoritzLaurer/deberta-v3-large-zeroshot-v1.1-all-33")

logger = logging.getLogger(__name__)

@router.post("")
async def text_classification(text: str) -> str:
    try:
        start_time = time.time()
        logger.info(f"stt 시작")

        ## finetunning을 위한 template
        hypothesis_template = "This record is about {}"

        ## 분류할 카테고리 리스트
        classes_verbalized = ["RESTAURANT", "SMALLTALK", "TRAVEL"]
        
        output = zeroshot_classifier(text, classes_verbalized, hypothesis_template=hypothesis_template, multi_label=False)

        result = output['labels'][0]

        end_time = time.time()
        logger.info(f"stt 끝 {end_time - start_time}초")
        return result
    except Exception as e:
        return str(e)
