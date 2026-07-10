import speech_recognition as sr
import whisper
import os
import sys
import numpy as np
import subprocess

class Ear:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.model = whisper.load_model("base", device="cpu")

    def suppress_noise(self):
        '''
            --- SILENCE LAYER ---
            If system issues arise and code seems to 'vanish' without error, 
            comment out the suppress_noise() call to check stderr.
        '''
        null_fd = os.open(os.devnull, os.O_WRONLY)
        os.dup2(null_fd, sys.stderr.fileno())

    def listen(self, timeout=5, phrase_time_limit=10):
        '''
        devices = sr.Microphone.list_microphone_names()
        print("Available microphones:")
        for i, device in enumerate(devices):
            print(f"  {i}: {device}")
        
        mic_name = "hw:0,7"
        device_index = None
        
        for i, name in enumerate(sr.Microphone.list_microphone_names()):
            if mic_name in name:
                device_index = i
                break
        
        print(f"Using microphone: {sr.Microphone.list_microphone_names()[device_index]}")
        '''
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                self.recognizer.pause_threshold = 1
                print("Listening...")
                audio_data = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                print("Recognizing...")
        except sr.WaitTimeoutError:
            print("Timeout reached.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return audio_data

    def audio_to_numpy(self,audio_data):
        process = subprocess.Popen(['ffmpeg', '-i', '-', '-f', 's16le', '-ac', '1', '-ar', '16000', '-'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        raw_audio, _ = process.communicate(input=audio_data.get_raw_data())
        audio_array = np.frombuffer(raw_audio, np.int16).flatten().astype(np.float32) / 32768.0
        return audio_array

    def transcribe(self, audio_array):
        if np.sum(np.abs(audio_array)) < 0.01:
            print("Debug: Silence detected.")
            return "[Silence Detected]"

        try:
            result = self.model.transcribe(audio_array)
            return result["text"]
        except Exception as e:
            print(f"An error occurred while transcribing: {e}")
            return ""

if __name__ == "__main__":
    test_ear = Ear()
    #test_ear.suppress_noise()
    audio_data = test_ear.listen()
    if audio_data:
        audio_array = test_ear.audio_to_numpy(audio_data)
        print(f"Debug: Audio array shape: {audio_array.shape}, dtype: {audio_array.dtype}, min: {np.min(audio_array)}, max: {np.max(audio_array)}")
        transcription = test_ear.transcribe(audio_array)
        print("Transcription: ", transcription)