# Django import
from django.http import JsonResponse
# Drf import
from rest_framework import generics 
from rest_framework import status

# Custom module import
from .models import Braille, Korean
from .serializers import BrailleSerializer, KoreanSerializer
from angelina_braille import website_recognizer
from tesseract.tesseract_abspath import path as tesseract_path

# Third party modules
import pytesseract
from BrailleToKorean.BrailleToKor import BrailleToKor
from PIL import Image
import cv2
import os


class BrailleCreateAPIView(generics.CreateAPIView):
    queryset = Braille.objects.all()
    serializer_class = BrailleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        img = serializer.data["image"][serializer.data["image"].index("media"):]
        img_name = img
        img_abs_path = os.path.join(os.path.join(os.getcwd()), img_name)

        temp = cv2.imread(img_abs_path)
        temp = cv2.resize(temp, dsize=(0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_LINEAR)
        
        h, w = temp.shape[:2]
        h1, h2 = int(h * 0.1), int(h * 0.9)
        w1, w2 = int(w * 0.1), int(w * 0.9)
        temp = temp[h1: h2, w1: w2]
        gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
        img2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
        contours = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

        x1 = [] #x좌표의 최소값
        y1 = [] #y좌표의 최소값
        x2 = [] #x좌표의 최대값
        y2 = [] #y좌표의 최대값
        
        for i in range(1, len(contours)):# i = 1 는 이미지 전체의 외곽이되므로 카운트에 포함시키지 않는다.
            ret = cv2.boundingRect(contours[i])
            x1.append(ret[0])
            y1.append(ret[1])
            x2.append(ret[0] + ret[2])
            y2.append(ret[1] + ret[3])
            
        x1_min = min(x1)
        y1_min = min(y1)
        x2_max = max(x2)
        y2_max = max(y2)
        cv2.rectangle(temp, (x1_min, y1_min), (x2_max, y2_max), (0, 255, 0), 3)

        temp = temp[y1_min:y2_max, x1_min:x2_max]
        
        cv2.imwrite(img_abs_path, temp)


        braille_text = website_recognizer.main(img_abs_path)
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
        img = os.path.join(os.path.join(os.getcwd()), img)


        
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
        text = pytesseract.image_to_string(img, lang="kor").replace("\n", " ")
        
        Korean.objects.get(id=serializer.data["id"]).delete()
        
        return JsonResponse({"text": text}, status=status.HTTP_201_CREATED)
    
    
