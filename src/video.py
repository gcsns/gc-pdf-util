import subprocess
from logger import logger
from openai import OpenAI
import openai
import os
import glob
import base64
import configs

def extract_audio_from_video(video_file_path: str, audio_file_path: str) -> str:
    """
    Extracts the audio from a video file path and stores it at a path specified by the user.

    Args:
        video_file_path (str): The path to the video file.
        audio_file_path (str): The path where the audio file will be stored.
    
    Returns:
        str: The audio file path.
    """

    # Extract audio using ffmpeg
    ffmpeg_command = [
        "ffmpeg",
        "-i", video_file_path,          # Input file
        "-vn",                     # No video
        "-acodec", "mp3",    # Audio codec
        "-b:a", "192k",              # Bitrate (optional, adjust as needed)
        audio_file_path                 # Output file
    ]
    subprocess.run(ffmpeg_command, check=True)

    return audio_file_path

def transcribe_audio(audio_file_path: str):
    """
    Transcribes the audio file at the specified path using the Whisper API.

    Args:
        audio_file_path (str): The path to the audio file to transcribe.

    Returns:
        json: The verbose transcribed text from the audio file.
    """

    openai.api_key = configs.OPENAI_API_KEY

    client = OpenAI()


    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format= 'verbose_json',
        )

    return transcript

def extract_frames(video_file_path: str, frames_dir: str, fps: float = 0.2):
    """
    Extracts frames at given fps from the video file at the specified path.

    Args:
        video_file_path (str): The path to the video file to extract frames from.
        frames_dir (str): The directory where the extracted frames will be saved.
        fps (float): The frames per second to extract frames at. Default is 0.2.

    Returns:
        images (list): A list of base64 encoded images.
    """

    os.makedirs(frames_dir, exist_ok=True)
    frame_pattern = f"{frames_dir}/frame_%04d.jpg"
    ffmpeg_frames_cmd = [
        "ffmpeg",
        "-i", video_file_path,
        "-vf", f"fps={fps}",
        "-loglevel", "error",
        frame_pattern
    ]
    subprocess.run(ffmpeg_frames_cmd, check=True)

    frame_files = sorted(glob.glob(f"{frames_dir}/*.jpg"))
    encoded_frames = []
    for frame_file in frame_files:
        with open(frame_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            encoded_frames.append(encoded_string)

    return encoded_frames



