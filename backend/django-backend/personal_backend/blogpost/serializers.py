from rest_framework import serializers
from .models import BlogModel, Category, Tag, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'author_id', 'author', 'created_at', 'updated_at', 'categories', 'tags', 'comments']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author_id', 'created_at', 'updated_at']