from django.contrib import admin
from .models import File, Words


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('file', 'upload_at', 'processed')


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    model = Words
    list_display = ('word', 'tf')
