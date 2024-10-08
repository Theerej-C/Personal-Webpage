from django.db import models

class BlogModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_id = models.BigIntegerField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='blog_posts',null=True)
    tags = models.ManyToManyField('Tag', related_name='blog_posts',null=True)
    comments = models.ManyToManyField('Comment', related_name='blog_posts',null=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Comment(models.Model):
    content = models.TextField()
    author_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)