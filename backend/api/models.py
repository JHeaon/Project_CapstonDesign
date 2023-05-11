from django.db import models

class Braille(models.Model):
    image = models.ImageField(upload_to='Braille/')

class Korean(models.Model):
    image = models.ImageField(upload_to='Korean/')