import logging
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .rabbitmq_utils import send_to_rabbitmq

from .message_patterns import choise_pattern

logger = logging.getLogger('views')

@api_view(['POST'])
def send_notify(request):
    logger.info('send_notify: VIEW IS CALLED!')
    try:
        resp = {}
        if request.method == 'POST':
            data = request.body.decode().split("****")
            pattern = choise_pattern(data)
            
            if pattern != None:
                text = pattern.message()
                
                if len(pattern.to_users()) > 0:
                    for user in pattern.to_users():
                        message = {
                            'user_id': user,
                            'type': pattern.notify_type,
                            'ticket_id': pattern.ticket_id,
                            'ticket_url': 'https://helpdesk.ics.perm.ru/front/ticket.form.php?id={}'.format(pattern.ticket_id),
                            'text': text,
                            'parse_mode': 'MARKDOWN'
                        }

                        send_to_rabbitmq('telegram_queue', message)

                        logger.info('send_notify: SENDED MESSAGE TO RABBIT MQ, data: user - %s, ticket - %s', user, pattern.ticket_id)
                else:
                    logger.info('send_notify: USERS IS NOT FOUND %s, ticket - %s', pattern.assign_user, pattern.ticket_id)
                    
            else:
                logger.warning('send_notify: MESSAGE PATTERN NOT FOUND')

        else:
            logger.warning('send_notify: INCORRECT REQUEST METHOD %s', request.method)

    except Exception as exc:
        logger.error('send_notify: ERROR %s', exc)
    
    resp['status'] = 200 #always return the 200 code, otherwise glpi will receive an error.
    return JsonResponse(resp)


class EmplyeesApiView(ModelViewSet):
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employees.objects.all()

    
    
