from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glpi_http.settings')

app = Celery('glpi_http')

# Загрузите настройки из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находите задачи в приложениях
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)