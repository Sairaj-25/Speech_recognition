# pip install -U openai-whisper
# pip install torch
# pip install pyaudio

import streamlit as st
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile

st.set_page_config(page_title="Whisper Speech recognition",page_icon="🎤")
st.title("OpenAI whisper")
st.write("speak 🎤")

# Load Whisper model (tiny | base | small | medium | large)
@st.cache_resource
def load_model():
    return whisper.load_model("small")  # higher accuracy

model = load_model()

SAMPLE_RATE = 16000
DURATION = 10 # max 10 seconds

def record_audio():
    audio = sd.rec(
        int(SAMPLE_RATE * DURATION),
        samplerate = SAMPLE_RATE,
        channels = 1,
        dtype = np.int16
    )
    sd.wait()
    return audio

def transcribe_audio(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, SAMPLE_RATE, audio)
        result = model.transcribe(f.name)
        return result["text"]
    
# Button
if st.button("🎤 Speak"):
    with st.spinner("Listening...🎧"):
        audio = record_audio()
        text = transcribe_audio(audio)

    st.subheader("Text 📝")
    st.success(text)

