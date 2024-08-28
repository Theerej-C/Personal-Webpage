from django.urls import path
from .views import blogpost_crud_api,blogpost_comment_api

urlpatterns = [
    path('crud/', blogpost_crud_api),
    path('comments/',blogpost_comment_api)
]
