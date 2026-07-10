import os
import sys
import whisper
import speech_recognition as sr
import numpy as np

class Ear:
    def __init__(self, model_size="base"):
        self.recognizer = sr.Recognizer()
        # Loading model on initialization
        self.model = whisper.load_model(model_size, device="cpu")
        self._suppress_stderr()

    def _suppress_stderr(self):
        """Silences stderr to keep the terminal clean."""
        null_fd = os.open(os.devnull, os.O_WRONLY)
        os.dup2(null_fd, sys.stderr.fileno())

    def listen(self):
        """Captures audio from the microphone."""
        with sr.Microphone(sample_rate=16000) as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            self.recognizer.pause_threshold = 1
            print("Listening...")
            last_audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=60)
            return last_audio.get_raw_data()
    
    def convert_to_float(self, raw_data):
        """Normalizes raw int16 data to float32."""
        audio_array = np.frombuffer(raw_data, dtype=np.int16)
        return audio_array.astype(np.float32) / 32768.0

    def transcribe(self, float_audio):
        """Transcribes the float32 audio array using Whisper."""
        result = self.model.transcribe(float_audio)
        return result["text"]

# Allows for direct execution or importing as a module
if __name__ == "__main__":
    ear = Ear()
    raw = ear.listen()
    data = ear.convert_to_float(raw)
    print("Transcription:", ear.transcribe(data))