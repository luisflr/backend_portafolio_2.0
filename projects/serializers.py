from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
  image = serializers.SerializerMethodField()
  
  class Meta:
    model = Projects
    fields = [
      'name',
      'description',
      'stack',
      'order',
      'image',
      'code_url',
      'demo_url',
      'type_project',
      'platform',
      'role',
      'team',
      'status'
    ]
  
  def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url