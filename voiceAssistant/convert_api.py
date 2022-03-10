import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы
import funcs




# Основной класс


def convert():
    class Currency:
        DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
        # Заголовки для передачи вместе с URL
        EUR_RUB = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1CHZN_ruRU991RU991&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+&aqs=chrome.0.0i131i433i512l2j69i57j0i131i433i512j0i512j0i131i433i512l2j0i512j0i131i433j0i512.2114j1j7&sourceid=chrome&ie=UTF-8'
        DOL_EUR = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&rlz=1C1CHZN_ruRU991RU991&ei=FwUqYrO2MJ-GwPAP9PCBwAg&ved=0ahUKEwjzndnh2rv2AhUfAxAIHXR4AIgQ4dUDCA4&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoOCC4QgAQQsQMQxwEQowI6CAgAEIAEELEDOgkIABCxAxAKEAE6CAguEIAEENQCOhEILhCABBCxAxCDARDHARDRAzoICAAQsQMQgwE6CwguEIAEEMcBENEDOgoIABCxAxCDARBDOgQIABBDOg4IABCABBCxAxCDARDJAzoPCAAQsQMQgwEQChBGEIICOgoIABCxAxCDARAKOgcIABCABBAKOg0IABCxAxCDARDJAxAKSgQIQRgASgQIRhgAUMsIWO4tYKQwaARwAXgAgAH5AYgBpRCSAQYxLjEzLjKYAQCgAQGwAQDAAQE&sclient=gws-wiz'
        EUR_DOL = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&rlz=1C1CHZN_ruRU991RU991&ei=MwUqYpG1Nq_1qwHM5IToCA&oq=%D0%B5%D0%B2%D1%80%D0%BE+&gs_lcp=Cgdnd3Mtd2l6EAMYADIPCAAQsQMQgwEQQxBGEIICMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIKCAAQsQMQgwEQQzIHCAAQyQMQQzIECAAQQzIECAAQQzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBOggIABCABBCxAzoICAAQsQMQgwFKBAhBGABKBAhGGABQgAdYvgxggRZoAXABeAGAAeUCiAG8C5IBBzAuMS4xLjOYAQCgAQGwAQDAAQE&sclient=gws-wiz'
        RUB_DOL = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&rlz=1C1CHZN_ruRU991RU991&ei=gwUqYvGeEpLdrgT2kp7ADg&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B4&gs_lcp=Cgdnd3Mtd2l6EAMYADILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgAEEM6CggAELEDEIMBEEM6EggAELEDEIMBEMkDEEMQRhCCAjoICAAQsQMQgwE6DggAEIAEELEDEIMBEMkDOhAIABCABBCxAxCDARBGEIICSgQIQRgASgQIRhgAUNYFWIcaYL8gaAFwAXgAgAF3iAHkB5IBAzAuOZgBAKABAbABAMABAQ&sclient=gws-wiz'
        RUB_EUR = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&rlz=1C1CHZN_ruRU991RU991&ei=lwUqYvygGeeprgSx-JywCQ&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B5%D0%B2&gs_lcp=Cgdnd3Mtd2l6EAMYADIQCAAQgAQQsQMQgwEQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQyQMyBQgAEIAEOgcIABBHELADOgoIABBHELADEMkDOgcIABCwAxBDOgoIABCxAxCDARBDOgsIABCABBCxAxCDAToPCAAQsQMQgwEQQxBGEIICOg4IABCABBCxAxCDARDJAzoHCAAQgAQQCkoECEEYAEoECEYYAFCDBljEF2D8ImgBcAF4AIABeYgB2QeSAQMwLjmYAQCgAQHIAQrAAQE&sclient=gws-wiz'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        curr = funcs.voice.split()
        if len(curr) > 4:
            curr = curr[1:]
        current_converted_price = 0


        def __init__(self):
            # Установка курса валюты при создании объекта
            try:
                self.current_converted_price = float(self.get_currency_price().replace(",", "."))
            except Exception:
                raise Exception

        # Метод для получения курса валюты
        def get_currency_price(self):
            global curr
            try:
                # Парсим всю страницу
                if self.curr[1] == 'долларов' and self.curr[3] == 'рубли':
                    full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
                elif self.curr[1] == 'рублей' and self.curr[3] == 'доллары':
                    full_page = requests.get(self.RUB_DOL, headers=self.headers)
                elif self.curr[1] == 'рублей' and self.curr[3] == 'евро':
                    full_page = requests.get(self.RUB_EUR, headers=self.headers)
                elif self.curr[1] == 'евро' and self.curr[3] == 'рубли':
                    full_page = requests.get(self.EUR_RUB, headers=self.headers)
                elif self.curr[1] == 'долларов' and self.curr[3] == 'евро':
                    full_page = requests.get(self.DOL_EUR, headers=self.headers)
                elif self.curr[1] == 'евро' and self.curr[3] == 'доллары':
                    full_page = requests.get(self.EUR_DOL, headers=self.headers)
                # Разбираем через BeautifulSoup
                soup = BeautifulSoup(full_page.content, 'html.parser')

                # Получаем нужное для нас значение и возвращаем его
                convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
                return convert[0].text
            except (UnboundLocalError, IndexError):
                funcs.speak("Скажите, к примеру: 50 долларов в рубли")
                raise Exception

        # Проверка изменения валюты
        def check_currency(self):
            try:
                currency = float(self.get_currency_price().replace(",", ".")) * float(curr[0])
                reformat_curr = str(curr).replace('[', '')
                reformat_curr = reformat_curr.replace(']', '')
                reformat_curr = reformat_curr.replace("'", '')
                reformat_curr = reformat_curr.replace(",", '')
                funcs.speak(str(reformat_curr) + ' по текущему курсу: ' + str(currency))
            except AttributeError:
                funcs.speak("Скажите, к примеру: 50 долларов в рубли")
                raise Exception
    curr = funcs.voice.split()
    if len(curr) > 4:
        curr = curr[1:]
    currency = Currency()
    currency.check_currency()
