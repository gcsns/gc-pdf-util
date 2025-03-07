from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
import subprocess
import openai
from openai import OpenAI
import os
import uuid
from typing import Dict
import glob
import base64
from logger import logger
from video import extract_audio_from_video, extract_frames, transcribe_audio
import configs

router = APIRouter(prefix="/video")

@router.post("/process-video")
async def processVideo(file: UploadFile = File(...)):
    # Generate unique filenames to avoid conflicts
    temp_id = str(uuid.uuid4())
    video_path = f"/tmp/{temp_id}_{file.filename}"
    audio_path = video_path.rsplit('.', 1)[0] + ".wav"
    frames_dir = f"/tmp/{temp_id}_frames"

    with open(video_path, "wb") as out_file:
        while chunk := await file.read(1024 * 1024):  # 1 MB chunks
            out_file.write(chunk)

    try:        
        # Extract audio
        audio_file_path = extract_audio_from_video(video_path, audio_path)
        logger.info("Audio file extracted at {}".format(audio_file_path))

        # Transcribe
        transcript = transcribe_audio(audio_file_path)
        logger.info("Transcription complete")

        # Extract frames
        frames = extract_frames(video_path, frames_dir)
        logger.info("Extracted frames at {}".format(frames_dir))

        return {"transcript": transcript, "frames": frames}

    except Exception as e:
        logger.info(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        try:
            # Remove the temporary files
            os.remove(video_path)
            os.remove(audio_path)
            os.removedirs(frames_dir)
        except Exception as e:
            logger.info(e)