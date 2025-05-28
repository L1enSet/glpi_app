from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

@api_view(['POST'])
def send_notify(request):
    resp = {}
    if request.method == 'POST':
        print(request.body)
        resp['status'] = 200
        return JsonResponse(resp)
    else:
        resp['status'] = 400
        return JsonResponse(resp)


    
    
