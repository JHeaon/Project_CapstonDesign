from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # url 경로 추가하시면 됩니다.
    path("", include("main.urls")),
]
