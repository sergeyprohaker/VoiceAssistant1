import os
import funcs


def startapp():
    try:
        if funcs.voice.split()[-1] == 'блокнот':
            app_name = ' notepad'
        elif funcs.voice.split()[-1] == 'рисования' or funcs.voice.split()[-1] == 'paint':
            app_name = ' mspaint'
        elif funcs.voice.split()[-1] == 'задач':
            app_name = ' taskmgr'
        elif funcs.voice.split()[-1] == 'проводник':
            app_name = ' explorer'
        os.system('start' + app_name)
    except NameError:
        print('Не удалось найти стандартную программу')
