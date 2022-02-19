import pyttsx3
import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
import datetime
import win32com.client as wincl
import time
import anekdot
import browser
import calc
import convert
import translate
import codecs
import weather_forecast
import startapp

roaming = os.getenv('APPDATA')
path = os.path.dirname(roaming) + '\Local\VoiceAssistant'
try:
    os.mkdir(path)
except OSError:
    pass
opts = {"alias": ("гдз", "решебник", "ответы"),
        "tbr": (
            'скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'поставь', 'переведи', "засеки",
            'запусти', 'сколько будет'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "начини"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "прекрати"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутка"),
             "calc": ('прибавить', 'умножить', 'разделить', 'степень', 'вычесть', 'поделить', 'х', '+', '-', '/'),
             "startapp": ('открой приложение', 'запусти приложение'),
             "conv": ("валюта", "конвертер", "доллар", 'руб', 'евро'),
             "internet": ("вк", "загугли", "сайт", 'вконтакте', "найди"),
             "translator": ("переводчик", "translate", "переведи"),
             "deals": ("как оно", 'сам'),
             "showReminder": ("какие дела", "мои дела", "сегодня"),
             "weather": ("погод", "прогноз"),
             "stopWork": ("пока", "связи", "стоп", 'свидания')}}
startTime = 0
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = "str"


def speak(what):
    print(what)
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(what)


def callback(recognizer, audio):
    try:
        global voice
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()

        print('Распознано: ' + voice)

        cmd = voice

        f = open(path+'/to_do_list.txt', 'a')
        f.write(str(datetime.datetime.now()) + ' ' + voice + '\n')
        f.close()
        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()
        voice = cmd
        # распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("Голос не распознан!")
    except sr.RequestError:
        print("Проверьте интернет соединение")


def listen():
    with m as source:
        r.adjust_for_ambient_noise(source)
    stop_listening = r.listen_in_background(m, callback)
    while True: time.sleep(0.1)


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


def execute_cmd(cmd):
    global startTime
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас {0}:{1}".format(str(now.hour), str(now.minute)))
    elif cmd == 'startapp':
        startapp.startapp()
    elif cmd == 'calc':
        calc.calculator()
    elif cmd == 'conv':
        convert.convertation()
    elif cmd == 'translator':
        translate.translate()
    elif cmd == 'stupid1':
        anekdot.fun()
    elif cmd == 'internet':
        browser.browser()
    elif cmd == 'startStopwatch':
        speak("Секундомер запущен")
        startTime = time.time()
    elif cmd == "stopStopwatch":
        if startTime != 0:
            Time = time.time() - startTime
            speak(f"Прошло {round(Time // 3600)} часов {round(Time // 60)} минут {round(Time % 60, 2)} секунд")
            startTime = 0
        else:
            speak("Секундомер не включен")
    elif cmd == "showReminder":
        f1 = codecs.open(path+'/to_do_list.txt', encoding='windows-1251')
        s = f1.readlines()
        print(s)
    elif cmd == "weather":
        weather_forecast.forecast()
    elif cmd == 'deals':
        speak('У меня все превосходно! Надеюсь, у вас тоже')
    elif cmd == 'stopWork':
        speak("Приятно было пообщаться! До свидания.")
        exit()
    else:
        print("Команда не распознана")
