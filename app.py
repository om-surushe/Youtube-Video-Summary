from __future__ import unicode_literals
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
import yt_dlp
import ffmpeg
import sys
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline


def download_from_url(url: str, output_file: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        stream = ffmpeg.input(output_file)
        stream = ffmpeg.output(stream, output_file.replace('.m4a', '.wav'))

# create a title
st.title("Youtube Video Summarizer")

# take youtube url as input
video_url = st.text_input("Enter the URL of the YouTube video")
file_name = "output"

if st.button("Summarize") and video_url != "":

    download_from_url(video_url, file_name)

    r = sr.Recognizer()

    video = sr.AudioFile(file_name + ".wav")

    with video as source:
        audio = r.record(source)

    result = r.recognize_whisper(audio)


    tokenizer = AutoTokenizer.from_pretrained(
        "philschmid/bart-large-cnn-samsum", model_max_length=1024)

    model = AutoModelForSeq2SeqLM.from_pretrained(
        "philschmid/bart-large-cnn-samsum")

    summarizer = pipeline(
        "summarization", model=model, tokenizer=tokenizer, framework="pt")


    # break the result into chunks of 1024 characters
    chunks = [result[i:i+1024] for i in range(0, len(result), 1024)]

    # summarize the chunks
    summary = []
    for chunk in chunks:
        summary.append(summarizer(chunk, max_length=150,
                    min_length=30, do_sample=False)[0]['summary_text'])

    # join the chunks
    summary = ''.join(summary)


    # convert the summary to audio and save it
    tts = gTTS(summary)
    tts.save("summary.mp3")

    # convert it to a format which could be played using st.audio
    st.audio("summary.mp3", format="audio/mp3")