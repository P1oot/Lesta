from django.contrib import admin
from .models import File, Words


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('file', 'name', 'upload_at', 'quantity', 'processed')


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    model = Words
    list_display = ('file_name', )

    def file_name(self, words):
        return words.file.name
