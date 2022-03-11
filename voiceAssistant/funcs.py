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
import convert_api
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
opts = {
        "tbr": (
            'скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'поставь', 'переведи', "засеки",
            'запусти', 'сколько будет', 'найти', 'найди', 'открой'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "начини"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "прекрати"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'знаешь анекдоты', "шутка"),
             "calc": ('прибавить', 'умножить', 'разделить', 'степень', 'вычесть', 'поделить', 'х', '+', '-', '/'),
             "startapp": ('открой приложение', 'запусти приложение'),
             "conv": ("конвертируй", "конвертер", "валют", "рубл", "евро", "доллар"),
             "internet": ("загугли", "сайт", "информацию о", "посоветуй"),
             "translator": ("переводчик", "translate", "переведи"),
             "deals": ("как оно", 'сам', 'дела'),
             "who": ('кто', "что", "ты"),
             "greet":("привет", "здравствуй"),
             "showReminder": ("лог", "история", "запросов"),
             "weather": ("погоды", "прогноз", "погода"),
             "stopWork": ("пока", "связи", "стоп", 'свидания'),
             "thanks": ("благодарю", "спасибо", "благодарен"),
             "help": ("помоги", "справка") }}

start_time = 0
speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[2].id)
r = sr.Recognizer()
m = sr.Microphone(device_index=1)
voice = "str"

def speak(what):
    """
    Prints the given text and speaks it using the windows speech API
    
    :param what: The text to speak
    """
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

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()
        voice = cmd
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("Голос не распознан или вы что-то некорректно произнесли! Попробуйте еще раз.")
    except sr.RequestError:
        speak("Кажется, у вас нет Интернета. Переключаю на оффлайн-распознавание...")
        os.system(r"C:\Users\Sergey\Downloads\offline_recognition.py")


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
    global start_time
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас {0}:{1}".format(str(now.hour), str(now.minute)))
    elif cmd == 'startapp':
        startapp.startapp()
        f = open(path + '/to_do_list.txt', 'a')
        f.write(str(datetime.datetime.now()) + ' ' + 'Программа успешно запущена!' + '\n')
        f.close()
    elif cmd == 'calc':
        calc.calculator()
    elif cmd == 'conv':
        convert_api.convert()
    elif cmd == 'translator':
        translate.translate()
        f = open(path + '/to_do_list.txt', 'a')
        f.write(str(datetime.datetime.now()) + ' ' + 'Слово переведено успешно' + '\n')
        f.close()
    elif cmd == 'stupid1':
        anekdot.fun()
    elif cmd == 'internet':
        browser.browser()
        f = open(path + '/to_do_list.txt', 'a')
        f.write(str(datetime.datetime.now()) + ' ' + 'Сайт открыт успешно' + '\n')
        f.close()
    elif cmd == 'startStopwatch':
        speak("Секундомер запущен")
        start_time = time.time()
    elif cmd == "stopStopwatch":
        if start_time != 0:
            Time = time.time() - start_time
            speak(f"Прошло {round(Time // 3600)} часов {round(Time // 60)} минут {round(Time % 60, 2)} секунд")
            start_time = 0
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
        quit()
    elif cmd == 'who':
        speak('Я - ваш голосовой помощник. Готова ответить на ваши вопросы в любое время')
    elif cmd == 'greet':
        speak('И тебе привет')
    elif cmd == 'thanks':
        speak('Была рада помочь! Обращайтесь еще.')
    elif cmd == 'help':
        print("Вот что я умею: отображение текущего времени, запуск / остановка секундомера, запуск стандартных \n"
              "приложений, посчитать что-нибудь на калькуляторе, поиск информации в Интернете, перевод слов с \n"
              "иностранных языков, выдать прогноз погоды в городе, конвертирование валют и рассказать анекдот")
    else:
        print("Команда не распознана")
