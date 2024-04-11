from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    FileUploadViewSet,
    FileListRetrieveViewSet,
    index,
    upload_file,
    file_words,
)

app_name = 'text_app'

router = SimpleRouter()
router.register('upload', FileUploadViewSet, basename='upload')
router.register('files', FileListRetrieveViewSet, basename='files')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
    path('upload/', upload_file, name='upload_file'),
    path('file/<int:file_id>', file_words, name='file_words'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
