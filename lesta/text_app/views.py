from rest_framework import viewsets, mixins
from .models import File
from .serializers import (FileUploadSerializer,
                          FileListSerializer,
                          FileRetrieveSerializer)
from .tasks import file_processing
from django.shortcuts import render, redirect
from .forms import FileForm
import requests
from rest_framework.response import Response
import json
from .func import make_paginator


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


def index(request):
    template = 'index.html'
    files_list = File.objects.all().order_by('-upload_at')
    page_obj = make_paginator(request, files_list)
    context = {
        'files': page_obj,
    }
    return render(request, template, context)


def upload_file(request):
    template = 'upload.html'
    form = FileForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        file = request.FILES['file']
        r = requests.post(
            'http://127.0.0.1:8000/api/upload/',
            files=[('file', file)],
        )
        if r.status_code == 201:
            return redirect('text_app:index')
        else:
            pass
            return render(request, template, {'form': form,
                                              'warning': True})
    else:
        return render(request, template, {'form': form})


def file_words(request, file_id):
    template = 'file_words.html'
    file_words_list_response = requests.get(
        'http://127.0.0.1:8000/api/files/'+str(file_id),
    )
    file_words_list = file_words_list_response.json()
    context = {
        'file': file_words_list,
    }
    return render(request, template, context)
