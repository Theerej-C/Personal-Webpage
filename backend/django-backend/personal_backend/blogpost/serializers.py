from rest_framework import serializers
from .models import BlogModel

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
    