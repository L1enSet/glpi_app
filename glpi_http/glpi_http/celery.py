from glpi_http.glpi_http.celery import Celery

app = Celery('glpi_http',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()