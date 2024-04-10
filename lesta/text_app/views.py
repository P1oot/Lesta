from rest_framework import viewsets, mixins
from .models import File
from .serializers import (FileUploadSerializer,
                          FileListSerializer,
                          FileRetrieveSerializer)
from .tasks import file_processing
from django.shortcuts import render, redirect
from .forms import FileForm
import requests


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
    queryset = File.objects.all().order_by('-upload_at')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FileRetrieveSerializer
        return FileListSerializer


def index(request):
    template = 'index.html'
    files_list = File.objects.all().order_by('-upload_at')
    context = {
        'files': files_list,
    }
    return render(request, template, context)


def upload_file(request):
    template = 'upload.html'
    form = FileForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        file = request.FILES['file']
        print(type(file))
        r = requests.post(
            'http://127.0.0.1:8000/api/upload/',
            files=[('file', file)],
            # data={'file': file},
        )
        if r.status_code == 201:
            return redirect('text_app:index')
        else:
            pass
            return render(request, template, {'form': form,
                                              'warning': True})
    else:
        return render(request, template, {'form': form})
