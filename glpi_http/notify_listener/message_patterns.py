from .utils import get_user_queryset
from bs4 import BeautifulSoup
from glpi_http.settings import django_tb
import telebot
from telebot import types

    

class UpdateTicketPattern():
    
    def __init__(self, data):
        self.notify_type = data[0]
        self.ticket_id = data[1]
        self.initiator = data[2]
        self.assign_user = data[3]
        self.title = data[4].replace("*", " ").replace("_", " ")
        self.description = data[5]
        self.initiator_obj = get_user_queryset(data[2])
        self.assign_user_obj = get_user_queryset(data[3])
    
    def parseDescription(self):
        try:
            soup = BeautifulSoup(self.description, 'lxml')
            result = ""
            for line in soup.find_all('p'):
                result += line.text
                result += "\n"
            return result.replace("*", " ").replace("_", " ")
        except Exception as exc:
            django_tb.send_message('631273289', str(exc))
            
    
    def message(self):
        
        """В Markdown-режиме для форматирования текста в telebot используются символы:

            * — жирный шрифт;

            _ — курсив;

            __ — подчёркивание;

            ~~ — зачёркнутый текст."""
        markup = types.InlineKeyboardMarkup()
        to_glpi_btn = types.InlineKeyboardButton("Посмотреть в GLPI {}".format(self.ticket_id), url='https://helpdesk.ics.perm.ru/front/ticket.form.php?id={}'.format(self.ticket_id))
        
        markup.add(to_glpi_btn)
        
        message = f"Обновление данных в заявке\n*Заявка:* {self.ticket_id}\n*Тема:* {self.title}\n\n*Описание:* {self.parseDescription()}\n*Инициатор:* _{self.initiator}_\n\n*Назначено специалистам:* _{self.assign_user}_"
        return (message, markup)
    
    def to_users(self):
        users_list = []
        if len(self.assign_user_obj) != 0:
            for user in self.assign_user_obj:
                users_list.append(user.tg_id)
        return users_list


def choise_pattern(data):
    patterns = {"update_ticket": UpdateTicketPattern}
    if data[0] in patterns.keys():
        return patterns[data[0]](data)