import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import action
#from rest_framework.response import Response


#from tg_bot.tg_bot_main import TOKEN, django_tb
from glpi_http.settings import django_tb, debug_tb
from .message_patterns import choise_pattern

@api_view(['POST'])
def send_notify(request):
    try:
        resp = {}
        if request.method == 'POST':
            debug_tb.send_message('631273289', request.body.decode()[0:200])
            data = request.body.decode().split("****")
            pattern = choise_pattern(data)
            if pattern != None:
                for user in pattern.to_users():
                    msg = pattern.message()
                    django_tb.send_message(user, msg[0], reply_markup=msg[1], parse_mode='MARKDOWN')
            else:
                resp['status'] = 400
                resp['error'] = 'User not found'
                django_tb.send_message('631273289', "#debug\npatter not found\n{}".format(request.body.decode()[0:50]))
                return JsonResponse(resp)
            
            resp['status'] = 200
            return JsonResponse(resp)
        else:
            resp['status'] = 400
            django_tb.send_message('631273289', "#debug\nrequest is not post\n{}".format(request.body.decode()[0:50]))
            return JsonResponse(resp)
    except Exception as exc:
        django_tb.send_message('631273289', str(exc))


class EmplyeesApiView(ModelViewSet):
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employees.objects.all()

    
    
