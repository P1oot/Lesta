from rest_framework import viewsets, mixins
from .models import File
from .serializers import (FileUploadSerializer,
                          FileListSerializer,
                          FileRetrieveSerializer)
from .tasks import file_processing
from rest_framework.response import Response
import json


class FileUploadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileUploadSerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.data.get('file').name)
        file_processing(serializer.data['id'])
        # file_processing.delay(serializer.data['id'])


class FileListRetrieveViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = File.objects.all().order_by('-upload_at')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FileRetrieveSerializer
        return FileListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        words_list = json.loads(serializer.data['words'][0]['words_list'])
        serializer.data['words'][0]['words_list'] = words_list
        return Response(serializer.data)
