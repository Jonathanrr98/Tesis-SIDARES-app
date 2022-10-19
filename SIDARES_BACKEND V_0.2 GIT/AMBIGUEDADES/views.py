
from fileinput import filename
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Ambiguedad, File
from AMBIGUEDADES.algoritmos import LexicaAnalisys, SyntacticAnalisys
from rest_framework.reverse import reverse


###############################

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AmbiguedadSerializers, UploadXlsSerializer
from rest_framework import status
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from .serializers import UploadSerializer
from rest_framework.viewsets import ViewSet
from django.core.files.storage import default_storage
import csv
import pandas as pd
import numpy as np
import json
from AMBIGUEDADES.algoritmos import DevolverFilas


###
fs = FileSystemStorage(location='tmp/')

# Create your views here.


class AmbiguedadesView(View):
    def get(self, request):
       
        lal = LexicaAnalisys.AddlexicalPolisemicalAmbiguety(request.GET['text'])
        las = SyntacticAnalisys.SyntacticAnalissys(request.GET['text'])
        las2 =SyntacticAnalisys.SyntacticAnalissys2(request.GET['text'])
  
        lamb = []
        lamb.extend(lal)
        lamb.extend(las)
        lamb.extend(las2)


        for x in lal:
            ambiguedad = Ambiguedad(
                tipo='ambiguedad lexica', descripcion=x, requisito=request.GET['text'])
            ambiguedad.save()

        for x in las:
            ambiguedad = Ambiguedad(
                tipo='ambiguedad sintáctica', descripcion=x, requisito=request.GET['text'])
            ambiguedad.save()

        for x in las2:
            ambiguedad = Ambiguedad(
                tipo='ambiguedad sintáctica', descripcion=x, requisito=request.GET['text'])
            ambiguedad.save()

        alist = Ambiguedad.objects.all()
        return JsonResponse(list(alist.values()), safe=False)


class FiltradoPorColumna(View):
    def get(self, request, format=None):
        colum_name = request.GET['cabecera']
        filename = File.objects.latest('id').file_name
        df = pd.read_csv(filename, sep=';',  encoding="utf-8")

        filter = df[colum_name].tolist()
        # print(filter)
        print(request)

        #cabecera = df.columns.tolist()

        z = ""
        for x in filter:
            lal = LexicaAnalisys.AddlexicalPolisemicalAmbiguety(x)
            las = SyntacticAnalisys.SyntacticAnalissys(x)
            las2 = SyntacticAnalisys.SyntacticAnalissys2(x)
            z = x
            # print(z)
            for y in lal:
                # print(z)
                ambiguedad = Ambiguedad(
                    tipo='ambiguedad lexica', descripcion=y, requisito=z)
                # print(z)
                ambiguedad.save()

            for y in las:
                ambiguedad = Ambiguedad(
                    tipo='ambiguedad sintáctica', descripcion=y, requisito=z)
                ambiguedad.save()

            for y in las2:
                ambiguedad = Ambiguedad(
                    tipo='ambiguedad sintáctica coordinativa', descripcion=y, requisito=z)
                ambiguedad.save()

        alist = Ambiguedad.objects.all()
        return JsonResponse(list(alist.values()), safe=False)


class Post_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        ambiguedad = Ambiguedad.objects.all()
        serializer = AmbiguedadSerializers(ambiguedad, many=True)

        return Response(serializer.data)

    def ambiguedad(self, request, format=None):
        serializer = AmbiguedadSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request, format=None, *args, **kwargs):
        ambiguedades = Ambiguedad.objects.all().delete()
        file = File.objects.all().delete()
        return JsonResponse(file,ambiguedades, safe=False) 

       


class Post_APIView_Detail(APIView):

    def get_object(self, pk):
        try:
            return Ambiguedad.objects.get(pk=pk)
        except Ambiguedad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ambiguedad = self.get_object(pk)
        serializer = AmbiguedadSerializers(ambiguedad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ambiguedad = self.get_object(pk)
        serializer = AmbiguedadSerializers(ambiguedad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ambiguedad = self.get_object(pk)
        ambiguedad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3


class File_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):

        filename = File.objects.latest('id').file_name
        df = pd.read_csv(filename, sep=';',  encoding="utf-8")

        cabecera = df.columns.tolist()

        df = pd.DataFrame(cabecera)
        dflist = df.to_numpy().tolist()

        # json = dflist.to_json(force_ascii=False, orient="values")
        flat_list = [item for l in dflist for item in l]
        # print(dflist)
        file = File.objects.all()

        return JsonResponse(list(flat_list), safe=False)
       


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        # print(request)
        #content_type = file_uploaded.content_type
        filename = "fileinfo/"+str(file_uploaded)  # received file name
        file_obj = request.data['file_uploaded']
        with default_storage.open(filename, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        df = pd.read_csv("media/"+filename, sep=';',  encoding="utf-8")

        cabecera = df.columns.tolist()

        df = pd.DataFrame(cabecera)

        json = df.to_json(force_ascii=False, orient="values")

        file = File(file_name="media/"+filename)
        file.save()
        files = File.objects.all()
        return JsonResponse(json, safe=False)


# Para EXELS
class UploadXlsViewSet(ViewSet):
    serializer_class = UploadXlsSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        fileexe_uploaded = request.FILES.get('fileexe_uploaded')
        # print(request)
        #content_type = file_uploaded.content_type
        filename = "fileinfo/"+str(fileexe_uploaded)  # received file name
        file_obj = request.data['fileexe_uploaded']
        with default_storage.open(filename, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        print(request)
        df = pd.read_excel("media/"+filename, )

        cabeceraexel = df.columns.tolist()

        df = pd.DataFrame(cabeceraexel)

        json = df.to_json(force_ascii=False, orient="values")

        file = File(file_name="media/"+filename)
        file.save()
        files = File.objects.all()
        return JsonResponse(json, safe=False)


