from django.db import models
from django.conf import settings
import jsonfield

# Create your models here.
class Order(models.Model): #model in which field has to be added       
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    json = jsonfield.JSONField()

    def __str__(self):
            return f"{self.id} - {self.user.id} - {self.datetime}"