
from rest_framework import serializers
from AMBIGUEDADES.models import Ambiguedad
from AMBIGUEDADES.models import File
from rest_framework.serializers import Serializer, FileField


class AmbiguedadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ambiguedad

        fields = ('id', 'tipo', 'descripcion', 'requisito')


# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ['is_removed', 'created', 'modified']

# para xls


class UploadXlsSerializer (Serializer):
    fileexe_uploaded = FileField()

    class Meta:
        fields = ['fileexe_uploaded']
