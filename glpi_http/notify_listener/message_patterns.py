from .utils import get_user_queryset



class UpdateTicketPattern1():
    
    def __init__(self, data):
        self.notify_type = data['notify_type']
        self.ticket_id = data['ticket_id']
        self.initiator = get_user_queryset(data['initiator'])
        self.assign_user = get_user_queryset(data['assign_user'])
        self.title = data['title']
        self.description = data['description']
    
    def message(self):
        message = f"Заявка - {self.ticket_id} была обновленна.\nТема - {self.title}\nОписание - {self.description}\nИнициатор - {self.initiator.fullName()}\nНазначено специалистам - {self.assign_user.fullName()}"
        return message
    
    def to_users(self):
        users_list = [self.assign_user.tg_id,]
        return users_list
    

class UpdateTicketPattern():
    
    def __init__(self, data):
        self.notify_type = data[0]
        self.ticket_id = data[1]
        self.initiator = get_user_queryset(data[2])
        self.assign_user = get_user_queryset(data[3])
        self.title = data[4]
        self.description = data[5]
    
    def message(self):
        message = f"Заявка - {self.ticket_id} была обновленна.\nТема - {self.title}\nОписание - {self.description}\nИнициатор - {self.initiator.fullName()}\nНазначено специалистам - {self.assign_user.fullName()}"
        return message
    
    def to_users(self):
        users_list = [self.assign_user.tg_id,]
        return users_list


def choise_pattern(data):
    patterns = {"update_ticket": UpdateTicketPattern}
    if data[0] in patterns.keys():
        return patterns[data["notify_type"]](data)