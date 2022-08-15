from django.db import models


# Create your models here.
class Noticia(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image  = models.CharField(max_length=500)