from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from .tasks import file_processing


class CreateListRetrieveMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    pass


class FileViewSet(CreateListRetrieveMixin):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.data.get('file').name)
        file_processing(serializer.data['id'])
        # file_processing.delay(serializer.data['id'])
