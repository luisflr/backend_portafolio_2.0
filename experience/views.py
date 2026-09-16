from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExperienceSerializer
from .models import Experience

class ExperienceViewSet(viewsets.ModelViewSet):
  serializer_class = ExperienceSerializer
  queryset = Experience.objects.all()
  
  