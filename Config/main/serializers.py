from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, ListField
from .models import BraiilePicture, KoreanPicture


class BraiilePictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BraiilePicture
        fields = '__all__'




class KoreanPictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = KoreanPicture
        fields = '__all__'
