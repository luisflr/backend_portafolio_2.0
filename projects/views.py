from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProjectsSerializer
from .models import Projects

class ProjectsViewSet(viewsets.ModelViewSet):
  serializer_class = ProjectsSerializer
  queryset = Projects.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly] 
  
  