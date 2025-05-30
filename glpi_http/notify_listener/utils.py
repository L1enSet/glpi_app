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
