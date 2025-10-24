import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile

def listen_from_microphone(duration=5, fs=44100):
    """
    Records audio from the microphone for a given duration using sounddevice,
    and returns the recognized text using SpeechRecognition.
    
    Parameters:
        duration (int): Recording duration in seconds (default 5s)
        fs (int): Sampling rate (default 44100 Hz)
    
    Returns:
        str: Recognized text from speech
    """
    print("Recording... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished.")

    # Save to a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        write(tmpfile.name, fs, recording)
        audio_file = tmpfile.name

    # Recognize speech using SpeechRecognition
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"
