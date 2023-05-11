# Django import
from django.http import JsonResponse
# Drf import
from rest_framework import generics 
from rest_framework import status

# Custom module import
from .models import Braille, Korean
from .serializers import BrailleSerializer, KoreanSerializer
from angelina_braille import website_recognizer

# Third party modules
import pytesseract
from BrailleToKorean.BrailleToKor import BrailleToKor
from dotenv import load_dotenv
import os

# load .env files
load_dotenv()


class BrailleCreateAPIView(generics.CreateAPIView):
    queryset = Braille.objects.all()
    serializer_class = BrailleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        img = serializer.data["image"][serializer.data["image"].index("media"):]
        braille_text = website_recognizer.main(img)
        translator = BrailleToKor()
        text = translator.translation(braille_text)
        
        Braille.objects.get(id=serializer.data["id"]).delete()
        
        return JsonResponse({"text": text}, status=status.HTTP_201_CREATED)
    

class KoreanCreateAPIView(generics.CreateAPIView):
    queryset = Korean.objects.all()
    serializer_class = KoreanSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        img = serializer.data["image"][serializer.data["image"].index("media"):]
        
        temp = os.getcwd() + r'/media/Korean/'
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        
        pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT")
        text = pytesseract.image_to_string(img, lang="kor+eng").replace("\n", " ")
        
        Korean.objects.get(id=serializer.data["id"]).delete()
        
        return JsonResponse({"text": text}, status=status.HTTP_201_CREATED)
    
    
