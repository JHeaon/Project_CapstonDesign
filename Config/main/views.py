# Django import
from django.http import JsonResponse
from django.shortcuts import render

# Drf import
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# 사용자 모듈 import
from .models import BraiilePicture, KoreanPicture
from .serializers import BraiilePictureSerializer, KoreanPictureSerializer
from .braiile import play
from .translate import PyJsHoisted_analyze_b_
from dotenv import load_dotenv

import os
import pytesseract


load_dotenv()

class BraiileVeiwSet(viewsets.ModelViewSet):
    '''
    2가지 설정이 필요
    1. braiile.py 의 chromedriver의 절대경로 변경해주기 
    2. 아래 변수 temp 절대경로 
    '''
    queryset = BraiilePicture.objects.all()
    serializer_class = BraiilePictureSerializer
    
    @action(detail=False, methods=['GET'])
    def translate(self, request):

        temp = os.getcwd() + r'/media/Braille/'
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        braille = play(full_name)
        answer = str(PyJsHoisted_analyze_b_(1, braille))
        os.remove(full_name)
        BraiilePicture.objects.all().delete()

        return JsonResponse({'answer': answer, 'braille': braille})
    
    
class KoreanVeiwSet(viewsets.ModelViewSet):
    queryset = KoreanPicture.objects.all()
    serializer_class = KoreanPictureSerializer
    
    @action(detail=False, methods=['GET'])
    def translate(self, request):

        temp = os.getcwd() + r'/media/Korean/'
        file_name = os.listdir(temp)[0]
        full_name = os.path.abspath(temp + "\\" + file_name)
        
        pytesseract.pytesseract.tesseract_cmd=os.getenv("TESSERACT")
        korean = pytesseract.image_to_string(full_name, lang="kor+eng")
        
        os.remove(full_name)
        KoreanPicture.objects.all().delete()
        
        return JsonResponse({'korean': korean})
    
