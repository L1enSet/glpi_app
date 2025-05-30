import requests
import json

def get_data():
    url = "http://172.17.1.26/send_notify/"
    url2 = "http://127.0.0.1:8000/send_notify/"
    headers = {'ContentType': 'text/plain'}
    data = {
        'notify_type': 'update_ticket',
        'ticket_id': '441959',
        'initiator':'Яковлев Антон Сергеевич',
        'assign_user': 'Яковлев Антон Сергеевич',
        'title': 'проблемы с ПК',
        'description': 'Активировать офис'
        }

    data2 = """update_ticket****0443676**** Яковлев Антон Сергеевич  **** Яковлев Антон Сергеевич  **** Проблемы с ПК  **** <div>\n<h1>Данные формы</h1>\n<h2>Информационный блок</h2>\n<div><strong>1) Описание обращения : </strong>\n<p>Тест. Не удалять. телеграм//////dfg</p>\n</div>\n</div>"""
    
    
    response=requests.post(url=url2, headers=headers, data=data2)
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

class UpdateTicketPattern1():
    
    def __init__(self, *args, **kwargs):
        self.notify_type = data['notify_type']
        self.ticket_id = data['ticket_id']
        self.initiator = data['initiator']
        self.assign_user = data['assign_user']
        self.title = data['title']
        self.description = data['description']


class UpdateTicketPattern():
    
    def __init__(self, data):
        self.notify_type = data[0]
        self.ticket_id = data[1]
        self.initiator = data[2]
        self.assign_user = data[3]
        self.title = data[4]
        self.description = data[5]
    
    def message(self):
        message = f"Заявка - {self.ticket_id} была обновленна.\nТема - {self.title}\nОписание - {self.description}\nИнициатор - {self.initiator}\nНазначено специалистам - {self.assign_user}"
        return message
    
    def to_users(self):
        users_list = [self.assign_user.tg_id,]
        return users_list


#data2 = """update_ticket****0443676**** Яковлев Антон Сергеевич  **** Яковлев Антон Сергеевич  **** Проблемы с ПК  **** <div>\n<h1>Данные формы</h1>\n<h2>Информационный блок</h2>\n<div><strong>1) Описание обращения : </strong>\n<p>Тест. Не удалять. телеграм//////dfg</p>\n</div>\n</div>  ****"""
#data = data2.split("****")
#cl = UpdateTicketPattern(data=data)
#print(cl.initiator.strip().split(" "))
#print(cl.assign_user.strip().split(" "))


kt = {'key':"123",}
try:
    print(kt["100"])
except Exception as exc:
    print(exc.__str__)
    print('hello')