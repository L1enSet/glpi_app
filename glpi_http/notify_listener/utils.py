from .models import Employees


def get_user_queryset(user_name):
    user_data = user_name.strip().split(" ")
    surname = user_data[0]
    name = user_data[1]
    patronymic = user_data[2]
    queryset = None
    try:
        queryset = Employees.objects.get(surname=surname, name=name, patronymic=patronymic)
    except Employees.DoesNotExist as exc:
        queryset = None
    return queryset

def create_message(data):
    notify_type = data['type']
    ticket_id = data['ticket_id']
    initiator = get_user_queryset(data['initiator'])
    assign_user = get_user_queryset(data['assign_user'])
    title = data['title']
    description = data['description']