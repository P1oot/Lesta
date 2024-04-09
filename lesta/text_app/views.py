from rest_framework import viewsets, mixins
# from rest_framework.response import Response
from .models import File
from .serializers import (FileUploadSerializer,
                          FileListSerializer,
                          FileRetrieveSerializer)
from .tasks import file_processing
# from django.shortcuts import render


class FileUploadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.data.get('file').name)
        file_processing(serializer.data['id'])
        # file_processing.delay(serializer.data['id'])


class FileListRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = File.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FileRetrieveSerializer
        return FileListSerializer
