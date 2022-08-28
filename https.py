import requests
import html2text
import re

while True:
    print('Ведите: 1 - для роботы з текстом "x" , 2 - для роботы з URL , 3 - поиск сылок')
    a = int(input('Ведите число :'))
    if a == 1:
        b = input('Ведите текст :')
        print('Функцыя в розработке следите за обновлениями .')
            # Убираем теги
        # Робота с текстом
    if a == 2:
        s = str(input('URL адрес :'))
        l = requests.get(s)
        print('HTML код :')
        print(l.text)
        # код URL
        f = int(input('Веди 1 чтобы убрать теги :'))
        if f == 1:
            d = html2text.HTML2Text()
            d.ignore_links = True
            c = d.handle(l.text)
            print('Текст HTML:')
            print(c)
            # Убираем теги "URL"
        # Робота с URL
    if a == 3:
        while True:
            string = str(input(''))
            if string == '3510':
                break
            pattern = r'\b(https:.+?)"'
            result = re.findall(pattern, string)
            print(result)
        # Поиск
