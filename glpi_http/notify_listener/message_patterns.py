from .utils import get_user_queryset
from bs4 import BeautifulSoup
from tg_bot.tg_bot_main import TOKEN, django_tb
    

class UpdateTicketPattern():
    
    def __init__(self, data):
        self.notify_type = data[0]
        self.ticket_id = data[1]
        self.initiator = data[2]
        self.assign_user = data[3]
        self.title = data[4]
        self.description = data[5]
        self.initiator_obj = get_user_queryset(self.initiator)
        self.assign_user_obj = get_user_queryset(self.assign_user)
    
    def parseDescription(self):
        try:
            soup = BeautifulSoup(self.description, 'lxml')
            result = ""
            for line in soup.find_all('p'):
                result += line.text
                result += "\n"
            return result
        except Exception as exc:
            django_tb.send_message('631273289', str(exc))
            
    
    def message(self):
        
        if self.initiator_obj != None:
            self.initiator = initiator_obj.fullName()
        if self.assign_user_obj != None:
            self.assign_user = self.assign_user_obj.fullName()
            
        message = f"Заявка - {self.ticket_id} была обновленна.\nТема - {self.title}\nОписание - {self.parseDescription()}\nИнициатор - {self.initiator}\nНазначено специалистам - {self.assign_user}"
        return message
    
    def to_users(self):
        users_list = []
        if self.assign_user_obj != None:
            users_list.append(self.assign_user.tg_id)
        return users_list


def choise_pattern(data):
    patterns = {"update_ticket": UpdateTicketPattern}
    if data[0] in patterns.keys():
        return patterns[data[0]](data)