from .models import Employees


"""def get_user_queryset(user_name):
    queryset = None
    try:
        user_data = user_name.strip().split(" ")
        surname = user_data[0]
        name = user_data[1]
        patronymic = user_data[2]
        try:
            queryset = Employees.objects.get(surname=surname, name=name, patronymic=patronymic)
        except Employees.DoesNotExist as exc:
            queryset = None
    except IndexError:
        queryset = None
    
    return queryset"""


def get_user_queryset(user_name):
    queryset_array = []
    try:
        users = []
        user_data = user_name.split(",")
        for user in user_data: 
            usr = {'surname': None,
                'name': None,
                'patronymic': None}
            index = 0
            for i in usr.keys():
                usr[i] = user.strip().split(" ")[index]
                index +=1
            users.append(usr)
        
        for user in users:    
            try:
                user = Employees.objects.get(surname=user['surname'], name=user['name'], patronymic=user['patronymic'])
                if user.is_active == True:
                    queryset_array.append(user)
            except Employees.DoesNotExist as exc:
                continue
    except IndexError as exc:
        queryset_array = []
        #tst
    
    print(queryset_array)
    
    return queryset_array
