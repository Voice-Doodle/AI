from pydantic import BaseModel

class TTSRequest(BaseModel):
    selected_voice: str
    content: str

