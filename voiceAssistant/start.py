import funcs
import datetime


now = datetime.datetime.now()

if 6 <= now.hour < 12:
    funcs.speak("Доброе утро! Чем я могу вам помочь?")
elif 12 <= now.hour < 18:
    funcs.speak("Добрый день! Чем я могу вам помочь?")
elif 18 <= now.hour < 23:
    funcs.speak("Добрый вечер!")
else:
    funcs.speak("Доброй ночи!")

funcs.listen()
