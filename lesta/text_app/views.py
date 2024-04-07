from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import File, Words
from .serializers import FileSerializer, WordsSerializer


class FileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class WordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
