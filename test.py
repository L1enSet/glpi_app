import requests

def get_data():
    url = "http://127.0.0.1:8000/send_notify/"
    headers = {'ContentType': 'json'}
    
    response=requests.post(url=url, headers=headers)
    print(response.status_code)

    print(response.text)

def strParse():
    string = """Update Ticket
ID: 0443676
Title: Проблемы с ПК
Заявка: Описание:  <div>\n<h1>Данные формы</h1>\n<h2>Информационный блок</h2>\n<div><strong>1) Описание обращения : </strong>\n<p>Тест. Не удалять. телеграм//////</p>\n</div>\n</div>  
Назначено специалистам: % Злыгостев Всеволод Львович  %"""
    a = string.split(" ")
    ticket = string.split('%')
    print(ticket[-2])

strParse()asdf