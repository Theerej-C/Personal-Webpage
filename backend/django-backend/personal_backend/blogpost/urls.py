from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, BlogPostGlobalViewSet, CommentViewSet, TagViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'crud-user', BlogViewSet, basename='blog')
router.register(r'retrieve-global', BlogPostGlobalViewSet, basename='blog-global')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
