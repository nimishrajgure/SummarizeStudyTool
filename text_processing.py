import os
import time
from pytube import YouTube
from txtai.pipeline import Summary
import whisper

def text_summary(text, maxlength=None):
    # Create summary instance
    summary = Summary()
    result = summary(text, maxlength=maxlength)
    return result

def download_and_transcribe_youtube_video(youtube_url, output_path, output_filename="custom_video_name.mp4"):
    try:
        yt = YouTube(youtube_url)
        ys = yt.streams.filter(only_audio=True).first()

        # Download video directly as MP4
        video_output_path = os.path.join(output_path, output_filename)
        ys.download(output_path, filename=output_filename)

        # Transcribe MP4 using Whisper
        start_time = time.time()
        model = whisper.load_model('base')
        out = model.transcribe(video_output_path)
        transcribed_text = out['text']
        end_time = time.time()
        print("Transcription time:", end_time - start_time, "seconds")

        return transcribed_text  # Return the transcribed text for summarization

    except Exception as e:
        print(f"Error: {e}")
        return None

def segment_text(text, segment_length=1000):
    # Split the text into segments based on the segment length
    segments = [text[i:i+segment_length] for i in range(0, len(text), segment_length)]
    return segments
