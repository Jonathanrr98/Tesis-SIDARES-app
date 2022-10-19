
from django.contrib import admin
from django.urls import path, include
from AMBIGUEDADES.views import  Post_APIView, Post_APIView_Detail,UploadViewSet, UploadXlsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('AMBIGUEDADES.urls')),
    path('', include(router.urls)),
    path('verambiguedades/', Post_APIView.as_view()),
    path('verambiguedadesid/<int:pk>/', Post_APIView_Detail.as_view()),


    

]
