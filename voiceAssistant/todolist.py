import datetime
import pyttsx3
import speech_recognition as sr
import time
import win32com.client as wincl

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = "str"


def callback(recognizer, audio):
    try:
        global voice
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()

        print('Распознано:' + voice)

    except sr.UnknownValueError:
        print("Голос не распознан!")


def listen():
    with m as source:
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(m, callback)
    while True: time.sleep(0.1)


def add_things():
    f = open("to_do_list.txt", 'w')
    f.write(str(datetime.datetime.now()) + ' ' + voice + '\n')
    if voice == "это все":
        f.close()

