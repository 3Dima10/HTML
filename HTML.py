import requests
import html2text

while True :
    s = str(input('URL адрес :'))
    a = requests.get(s)
    print('HTML код :')
    print(a.text)
    f = int(input('Веди 1 чтобы убрать теги :'))
    if f == 1 :
        d = html2text.HTML2Text()
        d.ignore_links = True
        c= d.handle(a.text)
        print('Текст HTML:')
        print(c)
