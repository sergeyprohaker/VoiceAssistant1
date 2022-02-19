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
        conditions = data['weather'][0]['description']
        funcs.speak(f"Условия {conditions}")
        temp = data['main']['temp']
        funcs.speak(f"Тепература {temp} градусов")
        min_temp = data['main']['temp_min']
        funcs.speak(f"Минимальная температура {min_temp} градусов")
        max_temp = data['main']['temp_max']
        funcs.speak(f"Максимальная температура {max_temp} градусов")

    except Exception as e:
        print("Exception (weather):", e)
        pass
