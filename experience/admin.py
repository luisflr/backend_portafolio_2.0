from django.contrib import admin
from .models import Experience

# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
  list_display = ('company', 'role', 'initial_date', 'end_date', 'description', 'achievements')
  search_fields = ('company', 'role')