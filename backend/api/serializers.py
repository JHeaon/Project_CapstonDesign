from rest_framework import serializers
from .models import Braille, Korean
from PIL import Image


class BrailleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Braille
        fields = "__all__"

class KoreanSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Korean
        fields = "__all__"
