from datetime import datetime
import gtts
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from sub import *
# import asyncio
import requests
import pygame


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
global_dict = {}

pygame.mixer.init()
sound = pygame.mixer.Sound('beep2.mp3')

def talk(text_str):
    tts = gtts.gTTS(text_str)
    # Save the audio file in the 'voice' directory
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    file_path = "voice/" + filename  # Concatenate the directory and filename
    tts.save(file_path)
    playsound(file_path)


# def is_wake_word(command):
#     return "catalyst" in command


def take_command_q():
    listener = sr.Recognizer()

    try:
        while True:
            with sr.Microphone() as source:
                print('Listening for wake word...')
                listener.adjust_for_ambient_noise(source)

                try:
                    voice = listener.listen(source, timeout=5)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if "catalyst" in command:
                        sound.play()
                        print('Wake word detected! Listening for command...')
                        voice = listener.listen(source, timeout=5)
                        command = listener.recognize_google(voice)
                        command = command.lower()
                        if "catalyst" in command:
                            command = command.replace('catalyst', '')
                            print(command)
                        return command

                except sr.WaitTimeoutError:
                    print("Listening timed out. Waiting for wake word again...")
                    continue

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


def run_alexa():
    command = take_command_q()
    print(f"Recognized command: {command}")
    if 'voice assistant' in command:
        #question1
        talk('How was you day? Was it Good, Bad or Ok? .')

        a1 = take_command_q()
        global_dict["ans1"] = a1
        print(a1)
        p1 = senti(a1)
        print(p1)
        if p1.get("polarity") > 0:
            print("positive")
        else:
            print("negative")
        print(wordfind(a1))
        #question 2
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('How are you feeling now?')
        a2 = take_command_q()
        global_dict["ans2"] = a2
        print(a2)
        p2 = senti(a2)
        print(p2)
        if p2.get("polarity") > 0:
            print("positive")
        else:
            print("negative")
        print(feelfind(a2))
        print(global_dict)
        #question3
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('Can you rate your mood out of 5? 1 is the worst 5 is great.')
        a3 = take_command_q()
        global_dict["ans3"] = a3
        r3 = analyze_mood(a3)
        talk("okey")
        #question4
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('Do you want to do anything about the above feelings?')
        a4 = take_command_q()
        global_dict["ans4"] = a4
        a41 = yes_no(a4)
        while 'repeat' in a41:
            talk('Yes or No answer will be much easy to understand')
            talk('Do you want to do anything about the above feelings?')
            a4 = take_command_q()
            a41 = yes_no(a4)
        talk(a41)
        #question5
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('What is happening in your mind and why?')
        a5 = take_command_q()
        # question6
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('What are the 5 things that you are grateful for?')
        a6 = take_command_q()
        # question7
        talk('you know, everything is good for something')
        talk('hmmmmmm')
        talk('Anything you want to share or note?')
        a7 = take_command_q()
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache. You better study Renewable Energy Module 4')
    elif 'hello' in command:
        talk('Hello, how are you')
    elif 'light' and 'on' in command:
        # Add your GET request here
        light_on_url = "https://blr1.blynk.cloud/external/api/update?token=RdPZKZXEmB59iMaBP2EYH75mw8afKzY3&D4=1"
        try:
            response = requests.get(light_on_url)
            if response.status_code == 200:
                talk("The light has been turned on.")
            else:
                talk("Failed to turn on the light.")
        except Exception as e:
            print(f"Error: {e}")
            talk("Failed to turn on the light. Please try again.")
    elif 'light' and 'off' in command:
        # Add your GET request here
        light_on_url = "https://blr1.blynk.cloud/external/api/update?token=RdPZKZXEmB59iMaBP2EYH75mw8afKzY3&D4=0"
        try:
            response = requests.get(light_on_url)
            if response.status_code == 200:
                talk("The light has been turned off.")
            else:
                talk("Failed to turn on the light.")
        except Exception as e:
            print(f"Error: {e}")
            talk("Failed to turn on the light. Please try again.")
    elif 'cheat' or 'exam' in command:
        print('Lemme dial up you')
        talk('Lemme dial up you')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

