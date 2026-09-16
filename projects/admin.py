from django.contrib import admin
from .models import Projects

# Register your models here.
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'stack', 'order', 'type_project')
  search_fields = ('name', 'type_project')