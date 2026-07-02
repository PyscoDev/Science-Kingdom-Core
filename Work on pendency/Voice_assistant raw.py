import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alpha' in command:
                command = command.replace('alpha', '')
            print(command)
    except:
        pass
    return command

def run_alpha():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        response = f"Sure, let me find {song} for you. I hope it brightens your day!"
        talk(response)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"Right now, it's {time}. Perfect time to be productive!"
        talk(response)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        response = f"Here's a brief on {person}: {info}. Fascinating, isn't it?"
        talk(response)
    elif 'date' in command:
        response = "I appreciate the offer, but let's keep it professional. How can I assist you today?"
        talk(response)
    elif 'are you single' in command:
        response = "I'm committed to helping you, always here for support!"
        talk(response)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        response = f"I've got a good one for you: {joke}. Hope that made you smile!"
        talk(response)

if __name__ == "_main_":
    run_alpha()
