class Notification:
    def __init__(self, users, text):
        self.users = users
        self.text = text


class EmployeeNotification(Notification):
    pass