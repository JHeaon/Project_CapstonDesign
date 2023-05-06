from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from . import views
from .views import *

from rest_framework import routers
from rest_framework import permissions

router = routers.DefaultRouter()
router.register('Braille', BraiileVeiwSet)
router.register('Korean', KoreanVeiwSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Statchung API",  # 제목
        default_version='v1',  # 버전
        description="Test description",  # 상세 설명
        terms_of_service="https://www.google.com/policies/terms/",  # 개인 정보 약관
        contact=openapi.Contact(email="contact@snippets.local"),  # 개발자 연락
        license=openapi.License(name="BSD License"),  # 라이 센스
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [

        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger',
                cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc',
                cache_timeout=0), name='schema-redoc')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
