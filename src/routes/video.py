from fastapi import FastAPI, UploadFile, File, HTTPException, APIRouter
import subprocess
import openai
from openai import OpenAI
import os
import uuid
from typing import Dict


router = APIRouter(prefix="/video")

# Make sure your OpenAI API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@router.post("/transcribe")
async def transcribe_video(file: UploadFile = File(...)):
    # Generate unique filenames to avoid conflicts
    temp_id = str(uuid.uuid4())
    video_path = f"/tmp/{temp_id}_{file.filename}"
    audio_path = video_path.rsplit('.', 1)[0] + ".wav"

    client = OpenAI()

    try:
        # Save uploaded video to disk
        with open(video_path, "wb") as f:
            f.write(await file.read())

        # Extract audio using ffmpeg
        ffmpeg_command = [
            "ffmpeg",
            "-i", video_path,          # Input file
            "-vn",                     # No video
            "-acodec", "pcm_s16le",    # Audio codec
            "-ar", "44100",            # Sample rate
            "-ac", "2",                # Channels
            audio_path                 # Output file
        ]
        subprocess.run(ffmpeg_command, check=True)

        

        # Transcribe audio with Whisper via OpenAI API
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file,
                response_format= 'verbose_json',
            )

        return {"transcript": transcript}

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error extracting audio: {e}")
    except openai.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"Error during transcription: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    finally:
        # Cleanup temp files
        for path in [video_path, audio_path]:
            if os.path.exists(path):
                os.remove(path)