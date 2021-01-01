
# Create your models here.
from django.db import models

class Image(models.Model):
    id=models.IntegerField(primary_key=True)
    url=models.IntegerField(max_length=100)

