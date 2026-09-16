from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProjectsSerializer
from .models import Projects

class ProjectsViewSet(viewsets.ModelViewSet):
  serializer_class = ProjectsSerializer
  queryset = Projects.objects.all()
  
  