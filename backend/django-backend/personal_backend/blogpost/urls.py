from django.urls import path
from .views import blogpost_crud_api

urlpatterns = [
    path('crud/', blogpost_crud_api)
]
