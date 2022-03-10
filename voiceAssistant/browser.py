import webbrowser
import funcs


def browser():
    site = funcs.voice
    s = funcs.voice.split()
    if 'сайт' in site:
        s.remove('сайт')
    elif 'информацию о' in site:
        s.remove('информацию')
        s.remove('о')
    elif "загугли" in site:
        s.remove('загугли')
    elif "посоветуй" in site:
        s.remove("посоветуй")
    s1 = str(s)
    new_s = s1.replace('[', '')
    new_s = new_s.replace(']', '')
    new_s = new_s.replace("'", '')
    new_s = new_s.replace(',', '')
    url = "https://yandex.ru/search/?lr=197&text=" + new_s
    webbrowser.get().open(url)
