import os
import sys
import subprocess
import numpy as np
import whisper
import speech_recognition as sr

null_fd = os.open(os.devnull, os.O_WRONLY)
os.dup2(null_fd, sys.stderr.fileno())

auditory_nerve = whisper.load_model("base",device="cpu")
ear = sr.Recognizer()

with sr.Microphone(sample_rate=16000) as source:
    ear.adjust_for_ambient_noise(source,duration=2)
    ear.pause_threshold = 1

    print("Listening...")
    last_audio= ear.listen(source, timeout=5, phrase_time_limit=10)
    raw_data = last_audio.get_raw_data()
'''
echo was not issue. sample rate was so no need for energy thrshold adjustment.
    ear.dynamic_energy_threshold = True
    ear.energy_threshold += 50
'''
    #print(raw_data)  #working till here getting the audio data in raw format(binary)

audio_array = np.frombuffer(raw_data, dtype=np.int16)
float_audio = audio_array.astype(np.float32) / 32768.0  # Normalizing to [-1.0, 1.0]

'''
print("Audio array shape:", float_audio.shape)
print("Audio array dtype:", float_audio.dtype)
print("The whole audio array:", float_audio)
#yes its working till here getting the audio data in raw format(binary) and then converting it to numpy array and then to float32 and normalizing it to [-1.0, 1.0] range for AI.
'''
result = auditory_nerve.transcribe(float_audio)
print("Transcription: ", result["text"])

##mission passed!Respect.😎😎