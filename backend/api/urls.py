from django.urls import path
from . import views

urlpatterns = [
    path('braille/', views.BrailleCreateAPIView.as_view()),
    path('korean/', views.KoreanCreateAPIView.as_view()),
]

