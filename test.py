import requests
import json

def get_data():
    url = "http://10.120.254.17/send_notify/"
    headers = {'ContentType': 'json'}
    data = {
        'notify_type': 'update_ticket',
        'ticket_id': '441959',
        'initiator':'Яковлев Антон Сергеевич',
        'assign_user': 'Яковлев Антон Сергеевич',
        'title': 'проблемы с ПК',
        'description': 'Активировать офис'
        }
    
    
    response=requests.post(url=url, headers=headers, data=json.dumps(data))
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

def get_user(user_name):
    user_data = user_name.strip().split(" ")
    surname = user_data[0]
    name = user_data[1]
    patronymic = user_data[2]
    print(user_data)

#get_user(" Злыгостев Всеволод Львович  ")


data = {
        'notify_type': 'update_ticket',
        'ticket_id': '441959',
        'initiator':'Яковлев Антон Сергеевич',
        'assign_user': 'Яковлев Антон Сергеевич',
        'title': 'проблемы с ПК',
        'description': 'Активировать офис'
        }

class UpdateTicketPattern():
    
    def __init__(self, *args, **kwargs):
        self.notify_type = data['notify_type']
        self.ticket_id = data['ticket_id']
        self.initiator = data['initiator']
        self.assign_user = data['assign_user']
        self.title = data['title']
        self.description = data['description']

get_data()