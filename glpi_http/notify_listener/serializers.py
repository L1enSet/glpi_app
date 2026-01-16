from rest_framework import serializers
from .models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Employees
		fields = ['id', 'glpi_token', 'glpi_name', 'tg_id', 'tg_name', 'surname', 'name', 'patronymic', 'is_active']