import webbrowser
import funcs


def translate():
    word = funcs.voice.split()[-1]
    url = "https://translate.google.com/?hl=ru&tab=TT&sl=auto&tl=ru&text=" + word + "&op=translate"
    webbrowser.get().open(url)

