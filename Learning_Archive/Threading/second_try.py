import pyttsx3
import time
import ollama
import threading
import sys
sys.path.append("/home/utsav-basu/Desktop/AGI/Git_Shared/Main/Custom_Modules")
from Ear import Ear
from Servo_180 import Servo_180

is_speaking = True
jaw_servo = Servo_180(15,50,0,180,3200,8200)
voice = pyttsx3.init()
voice.setProperty('rate',150)
voice.setProperty('volume',1.0)

def hearing():
    ear = Ear()
    raw = ear.listen()
    data = ear.convert_to_float(raw)
    in_info = ear.transcribe(data)
    return in_info

def get_response(question):
    response_model = ollama.chat(model = 'hermes3:latest', messages = [{'role':'user','content':question}])
    response = response_model['message']['content']
    return response

def written_reply(response):
    print(response)

def jaw_movement():
    global is_speaking
    jaw_servo.set_angle(0)
    while is_speaking:
        jaw_servo.set_angle(90)
        time.sleep(1)
        jaw_servo.set_angle(0)
        time.sleep(2)

def speak(response):
    global is_speaking
    is_speaking = True
    moving_jaw = threading.Thread(target=jaw_movement)
    writing_reply = threading.Thread(target = written_reply,args = (response,))
    moving_jaw.start()
    writing_reply.start()
    voice.say(response)
    voice.runAndWait()
    is_speaking = False

if __name__ == "__main__":
    is_speaking = False
    while not is_speaking:
        user_input = hearing()
        llm_response= get_response(user_input)
        speak(llm_response)