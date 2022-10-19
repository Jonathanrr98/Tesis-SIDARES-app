from django.urls import path
from .views import AmbiguedadesView
from .views import File_APIView,UploadXlsViewSet
from .views import UploadViewSet
from .views import FiltradoPorColumna


app_name = 'AMBIGUEDADES'


urlpatterns = [
  path('ambiguedades/', AmbiguedadesView.as_view(), name='ambiguedades_list'),

  path('file', UploadViewSet.as_view({'get': 'list'}),name='file'),

  path('colum', File_APIView.as_view(),name='colum'),

  path('filter', FiltradoPorColumna.as_view(),name='filter'),

  path('uploadxlsx/', UploadXlsViewSet.as_view({'get': 'list'})),

 
    






]
