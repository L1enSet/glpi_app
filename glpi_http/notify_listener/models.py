from django.db import models

class Employees(models.Model):
    glpi_token = models.CharField(max_length=256, null=True, blank=True)
    glpi_name = models.CharField(max_length=128, unique=True)
    tg_id = models.CharField(max_length=128, unique=True)
    tg_name = models.CharField(max_length=256, unique=True)
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.glpi_name} - {self.tg_name}"
    
    def fullName(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)
