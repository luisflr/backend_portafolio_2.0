from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectsViewSet

router = DefaultRouter()
router.register(r'projects', ProjectsViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
]
