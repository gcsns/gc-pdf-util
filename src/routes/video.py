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



router = APIRouter(prefix="/video")

# Make sure your OpenAI API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


@router.post("/process-video")
async def process_video(file: UploadFile = File(...)):
    # Generate unique filenames to avoid conflicts
    temp_id = str(uuid.uuid4())
    video_path = f"/tmp/{temp_id}_{file.filename}"
    audio_path = video_path.rsplit('.', 1)[0] + ".wav"
    frames_dir = f"/tmp/{temp_id}_frames"

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

        logger.info("Transcription Complete")
        logger.info(transcript.text)

        # Extract frames at 0.2 fps (1 frame every 5 seconds)
        os.makedirs(frames_dir, exist_ok=True)
        frame_pattern = f"{frames_dir}/frame_%04d.jpg"
        ffmpeg_frames_cmd = [
            "ffmpeg",
            "-i", video_path,
            "-vf", "fps=0.2",
            "-loglevel", "error",
            frame_pattern
        ]
        subprocess.run(ffmpeg_frames_cmd, check=True)

        logger.info(f"Extracted frames to {frames_dir}")
        
        
        # Read and encode frames as base64
        frame_files = sorted(glob.glob(f"{frames_dir}/*.jpg"))
        encoded_frames = []
        for frame_file in frame_files:
            with open(frame_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                encoded_frames.append(encoded_string)


        return {
            "transcript": transcript,
            "frames": encoded_frames
        }

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