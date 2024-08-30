from django.urls import path
from .views import blogpost_crud_api,blogpost_comment_api,blogpost_retrival_global_api

urlpatterns = [
    path('crud-user/', blogpost_crud_api),
    path('comments/',blogpost_comment_api),
    path('retrieve-global/',blogpost_retrival_global_api)
]
