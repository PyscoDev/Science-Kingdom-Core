import os
import sys
import whisper
import speech_recognition as sr
import numpy as np

class Ear:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.model = whisper.load_model("base", device="cpu")
        self.suppress_noise()

    def suppress_noise(self):
        null_fd = os.open(os.devnull, os.O_WRONLY)
        os.dup2(null_fd, sys.stderr.fileno())

    def listen(self):
        with sr.Microphone(sample_rate=16000) as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.recognizer.pause_threshold = 1
            print("Listening...")
            last_audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=60)
            raw_data = last_audio.get_raw_data()
            return raw_data
    
    def convert_to_float(self, raw_data):
        audio_array = np.frombuffer(raw_data, dtype=np.int16)
        float_audio = audio_array.astype(np.float32) / 32768.0  # Normalizing to [-1.0, 1.0]
        return float_audio

    def transcribe(self, float_audio):
        result = self.model.transcribe(float_audio)
        return result["text"]

if __name__ == "__main__":
    ear = Ear()
    raw_data = ear.listen()
    float_audio = ear.convert_to_float(raw_data)
    transcription = ear.transcribe(float_audio)
    print("Transcription: ", transcription)