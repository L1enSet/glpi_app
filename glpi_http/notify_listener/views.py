import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Employees
#from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAdminUser
#from rest_framework.decorators import action
#from rest_framework.response import Response


from tg_bot.tg_bot_main import TOKEN, django_tb
from .message_patterns import choise_pattern

@api_view(['POST'])
def send_notify(request):
    resp = {}
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        pattern = choise_pattern(data)
        print(pattern.to_users())
        if pattern != None:
            for user in pattern.to_users():
                django_tb.send_message(user, pattern.message())
        else:
            resp['status_code'] = 404
            resp['error'] = 'User not found'
            return JsonResponse(resp)
        
        resp['status_code'] = 200
        return JsonResponse(resp)
    else:
        resp['status_code'] = 400
        return JsonResponse(resp)


    
    
