"""
URL configuration for glpi_http project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notify_listener.views import send_notify, EmplyeesApiView
from rest_framework.routers import SimpleRouter, DefaultRouter


router = SimpleRouter()
router.register('employees', EmplyeesApiView, basename='employees')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_notify/', send_notify, name='send_notify'),
] + router.urls
#http://10.120.254.17/send_notify/