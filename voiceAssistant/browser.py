import webbrowser
import funcs


def browser():
    site = funcs.voice.split()[-1]
    open_tab = "https://yandex.ru/search/?lr=197&text=" + site
    webbrowser.get().open(open_tab)