from .models import File
from django.shortcuts import render, redirect
from .forms import FileForm
import requests
from .func import make_paginator


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
