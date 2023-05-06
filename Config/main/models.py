from django.db import models

# Create your models here.


class BraiilePicture(models.Model):
    image = models.ImageField(upload_to='Braille/', null=True)
    braille = models.CharField(max_length=255, null=True)


class KoreanPicture(models.Model):
    image = models.ImageField(upload_to='Korean/', null=True)
    korean = models.CharField(max_length=255, null=True)