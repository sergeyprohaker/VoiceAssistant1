import requests
import funcs


def forecast():
    if funcs.voice.split()[-1] == 'москве':
        s_city = 'Moscow,RU'
    elif funcs.voice.split()[-1] == 'сочи':
        s_city = 'Sochi'
    elif funcs.voice.split()[-1] == 'новосибирске':
        s_city = 'Novosibirsk'
    elif funcs.voice.split()[-1] == 'барнауле':
        s_city = 'Barnaul'
    else:
        funcs.speak("Не удалось распознать город, пожалуйста, введите его вручную")
        s_city = input("Введите название города транслитом с заглавной буквы: ")
    city_id = 0
    appid = "my_token"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        funcs.speak("Текущая погода:")
        conditions = data['weather'][0]['description']
        funcs.speak(f"Условия: {conditions}")
        temp = data['main']['temp']
        funcs.speak(f"Температура {temp} градусов")
        min_temp = data['main']['temp_min']
        funcs.speak(f"Минимальная температура {min_temp} градусов")
        max_temp = data['main']['temp_max']
        funcs.speak(f"Максимальная температура {max_temp} градусов")
        feels_like = data['main']['feels_like']
        funcs.speak(f'Ощущается как {feels_like} градусов')
        pressure = data['main']['pressure']
        funcs.speak(f'Давление {pressure}')
        humidity = data['main']['humidity']
        funcs.speak(f'Влажность {humidity} процентов')
        wind_speed = data['wind']['speed']
        funcs.speak(f'Скорость ветра {wind_speed} метров в секунду')

    except Exception as e:
        print("Exception (weather):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        funcs.speak("Почасовой прогноз на 5 дней: ")
        for i in data['list']:
            print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
    except Exception as e:
        print("Exception (forecast):", e)
        pass
