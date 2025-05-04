# ================================================
# Cloelia AI – Emotion Analysis Route
# Project: Eyes Unclouded / Atlas Signature
# Description: POST endpoint to receive an emotion
# Created: May 3, 2025
# Author: Khaylub Thompson-Calvin
# ================================================

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class EmotionPayload(BaseModel):
    emotion: str

@app.post("/analyze-emotion")
def analyze_emotion(payload: EmotionPayload):
    return { "message": f"Emotion '{payload.emotion}' received successfully" }
