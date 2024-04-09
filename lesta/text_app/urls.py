from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FileViewSet

router = SimpleRouter()
router.register('upload', FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
