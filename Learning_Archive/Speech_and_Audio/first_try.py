import os
import sys
import whisper
import speech_recognition as sr

def suppress_noise():
    null_fd = os.open(os.devnull, os.O_WRONLY)
    os.dup2(null_fd, sys.stderr.fileno())    

auditory_nerve = whisper.load_model("base",device="cpu")
ear = sr.Recognizer()

'''
 --- SILENCE LAYER ---
 If system issues arise and code seems to 'vanish' without error, 
comment out the suppress_noise() call to check stderr.
'''

suppress_noise() 

with sr.Microphone() as source:
    print(f"Microphone device index: {source.device_index}")
    print(f"Sample Rate: {source.SAMPLE_RATE}")
    print(f"Chunk size: {source.CHUNK}")
    ear.adjust_for_ambient_noise(source,duration=1)
    ear.pause_threshold = 1
    print("Listening...")
    audio_data = ear.listen(source, timeout=5, phrase_time_limit=10)
    print("Recognizing...")
with open("last_audio.wav", "wb") as file:
    file.write(audio_data.get_wav_data())

result = auditory_nerve.transcribe("last_audio.wav")
print("Transcription: ", result["text"])