from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ExperienceSerializer
from .models import Experience

class ExperienceViewSet(viewsets.ModelViewSet):
  serializer_class = ExperienceSerializer
  queryset = Experience.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]
  