from django.urls import path
from .views import user_login_view,user_registration_view,user_test_view

urlpatterns = [
    path('registration/',user_registration_view),
    path('login/',user_login_view),
    path('test',user_test_view)
]
