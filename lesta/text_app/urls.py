from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FileViewSet, WordsViewSet

router = SimpleRouter()
router.register('upload', FileViewSet)
router.register('words', WordsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
