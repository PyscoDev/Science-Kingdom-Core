import time
import threading
import pyttsx3
import subprocess

Welcoming= "Hello! How are you doing?"
def greet(greeting):
    text_to_speak = greeting + "\n"
    subprocess.run(["festival", "--tts"], input=text_to_speak.encode())
def show(greeting):
    print(greeting)

the_thread=threading.Thread(target=greet,args=(Welcoming,))

the_thread.start()

show(Welcoming)

