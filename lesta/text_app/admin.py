from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    model = File
    list_display = ('file', 'name', 'upload_at', 'processed')
