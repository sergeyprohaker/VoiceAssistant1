from googletrans import Translator
import funcs


def translate():
    trans = Translator()
    t = funcs.voice.split()[1:]
    funcs.speak(t)
    s = str(t)
    s1 = s.replace('[', '')
    s2 = s1.replace(']', '')
    s3 = s2.replace("'", '')
    result = trans.translate(s3, src='ru', dest='en')
    funcs.speak(result.origin + 'по-английски будет' + result.text)
