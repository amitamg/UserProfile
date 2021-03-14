from django.db import models

# Create your models here.


class CintaUser(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=False, default=18)
    skills = models.JSONField(default=dict)
    image1 = models.FileField(upload_to='')
    image2 = models.FileField(upload_to='')
