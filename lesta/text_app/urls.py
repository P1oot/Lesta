from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FileUploadViewSet, FileListRetrieveViewSet

router = SimpleRouter()
router.register('api/upload', FileUploadViewSet, basename='upload')
router.register('api/files', FileListRetrieveViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls))
]
