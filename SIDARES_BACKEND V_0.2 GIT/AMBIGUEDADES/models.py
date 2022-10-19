from asyncio.windows_events import NULL
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


class Ambiguedad(models.Model):
    tipo = models.CharField(max_length=5000 , default="")
    descripcion = models.TextField(max_length=5000, default="")
    requisito= models.TextField(max_length=5000, default='')


# rey
class File(models.Model):
    file_name = models.TextField(max_length=5000, null=False, blank=True)
    # classification = models.TextField(max_length=5000, null=False, blank=True)
    # status = models.TextField(max_length=5000, null=False, blank=True)
    # datetime = models.DateTimeField()



