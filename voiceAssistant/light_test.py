import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        # r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
    try:
        return r.recognize_google(audio, language='ru-RU')
    except:
        return None
    # return input()


def get_answer(text, _talk=True):
    if _talk:
        talk(text)
    while True:
        ans = listen()
        if ans is not None:
            print('Ответ:', ans)
            return ans.lower()
        else:
            talk('Простите, я вас не понял. Повторите еще раз.')


def get_indications_names(ans):
    qst = 'Если я правильно понял, вы хотите сдать показания '
    p = ['вода', 'воду', 'воды', 'воде', 'газ', 'газа', 'газу', 'электричество', 'электричеству', 'электричества',
         'отопление', 'отопления', 'отоплению']
    flag = False
    for i in p:
        if i[0] == 'в' and i in ans and 'воды' not in qst:
            qst += 'воды, '
            indications_names.append('воды')
            flag = True
        elif i[0] == 'г' and i in ans and 'газа' not in qst:
            qst += 'газа, '
            indications_names.append('газа')
            flag = True
        elif i[0] == 'о' and i in ans and 'отопления' not in qst:
            qst += 'отопления, '
            indications_names.append('отопления')
            flag = True
    if flag:
        return qst + '. Всё верно?'
    else:
        return 'Я вас не понимаю.'


def save_indications(ans, type):
    if any(i == ans for i in ['да', 'конечно', 'все верно', 'всё верно']):
        pass

    q = [ans.find(i) for i in ('горячая', 'горячей', 'горячую')]
    flag = False
    for i in q:
        if i >= 0:
            for j in ans:
                if j.isdigit():
                    received_indications['hot water'] += j
                elif received_indications['hot water']:
                    flag = True
                    break
        if flag:
            break

    q = [ans.find(i) for i in ('холодная', 'холодной', 'холодную')]
    flag = False
    for i in q:
        if i >= 0:
            for j in ans:
                if j.isdigit():
                    received_indications['cold water'] += j
                elif received_indications['cold water']:
                    flag = True
                    break
        if flag:
            break

    q = [ans.find(i) for i in ('отопление', 'отопления', 'отоплению')]
    flag = False
    for i in q:
        if i >= 0:
            for j in ans:
                if j.isdigit():
                    received_indications['heating'] += j
                elif received_indications['heating']:
                    flag = True
                    break
        if flag:
            break

    q = [ans.find(i) for i in ('газ', 'газа', 'газу')]
    flag = False
    for i in q:
        if i >= 0:
            for j in ans:
                if j.isdigit():
                    received_indications['gas'] += j
                elif received_indications['gas']:
                    flag = True
                    break
        if flag:
            break


def get_question(ans):
    global indications_names
    while True:
        if (any(i == ans for i in ['нет']) or any(i in ans for i in ['не верно'])) and \
           (question.endswith('. Всё верно?')):
            indications_names = []
            return 'Какие показания вы готовы сдать?'
        elif (any(i == ans for i in ['да', 'конечно']) or any(i in ans for i in ['все верно', 'всё верно'])) and \
             (question.endswith('. Всё верно?')):
            if 'воды' in indications_names and (not received_indications['hot water'] or not received_indications['cold water']):
                save_indications(ans, 'water')
                '''###########################################################
                if not bool_dict['cold water']:
                    if not bool_dict['hot water']:
                        return f'Холодная вода {received_indications["cold water"]}, горячая вода {received_indications["hot water"]}. Все правильно?'
                    return f'Холодная вода {received_indications["cold water"]}. Все правильно?'
                elif not bool_dict['hot water']:
                    return f'Горячая вода {received_indications["hot water"]}. Все правильно?'
                ###########################################################'''
                return 'Назовите показания холодной и горячей воды.'
            elif 'газа' in indications_names and not received_indications['gas']:
                save_indications(ans, 'gas')
                return 'Назовите показания газа.'
            elif 'отопления' in indications_names and not received_indications['heating']:
                save_indications(ans, 'heating')
                return 'Назовите показания отопления.'

        if question.startswith('Назовите показания '):
            if 'воды' in indications_names and not (received_indications['hot water'] or not received_indications['cold water']):
                save_indications(ans, 'water')
                if 'газа' in indications_names and not received_indications['gas']:
                    return 'Назовите показания газа.'
                elif 'отопления' in indications_names and not received_indications['heating']:
                    return 'Назовите показания отопления.'
                else:
                    talk('Все показания приняты. Спасибо, до свидания.')
                    exit()
            elif 'газа' in indications_names and not received_indications['gas']:
                save_indications(ans, 'gas')
                if 'воды' in indications_names and (not received_indications['hot water'] or not received_indications['cold water']):
                    return 'Назовите показания холодной и горячей воды.'
                elif 'отопления' in indications_names and not received_indications['heating']:
                    return 'Назовите показания отопления.'
                else:
                    talk('Все показания приняты. Спасибо, до свидания.')
                    exit()
            elif 'отопления' in indications_names and not received_indications['heating']:
                save_indications(ans, 'heating')
                if 'газа' in indications_names and not received_indications['gas']:
                    return 'Назовите показания газа.'
                elif 'воды' in indications_names and (not received_indications['hot water'] or not received_indications['cold water']):
                    return 'Назовите показания холодной и горячей воды.'
                else:
                    talk('Все показания приняты. Спасибо, до свидания.')
                    exit()

        elif any(i in ans for i in ['сдать показани', 'сдать свои показани', 'сдам показани', 'сдам свои показани']) and \
             any(i in ans for i in ['хочу', 'хотел', 'можно мне', 'можно я']):
            return 'Какие показания вы готовы сдать?'
        elif any(i in ans for i in ['как тебя зовут', 'как вас зовут', 'как тебя звать', 'как вас звать', 'своё имя',
                                    'ваше имя', 'как мне к вам обращаться', 'как мне к тебе обращаться', 'ты кто', 'кто ты']):
            return 'Меня зовут Давид. Я всегда рад вашим деньгам. Ой! Хотел сказать показаниям.'
        elif any(i in ans for i in ['кто тебя создал', 'кто вас создал', 'кто твой создатель', 'кто ваш создатель']):
            return 'Меня создали славные программисты из великого града Барнаула.'
        elif question == 'Какие показания вы готовы сдать?':
            qst = get_indications_names(ans)
            return qst
        elif 'давид' in ans:
            return 'Я рад, что вы запомнили моё имя.'
        else:
            talk('Я вас не понял. Повторите сказанное отчетливей, или перефразируйте ответ так, чтобы он был более понятен мне.')
            ans = get_answer(question, _talk=False)


indications_names = []
received_indications = {'hot water': '',
                        'cold water': '',
                        'gas': '',
                        'heating': ''}
bool_dict = {'hot water': '',
              'cold water': '',
              'gas': '',
              'heating': ''}

question = f'Здравствуйте. Чем я могу вам помочь?'
answer = get_answer(question)
while True:
    question = get_question(answer)
    answer = get_answer(question)