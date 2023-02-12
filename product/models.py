from django.db import models
from django.utils.html import mark_safe
import uuid


# Create your models here.
class Product(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return filename
    
    def img_preview(self):
        return mark_safe(f'<img style="max-width=300px; max-height: 300px;" src="{self.image_name.url}" />')


    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    image_name = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return f"{self.name} - {self.price}лв"