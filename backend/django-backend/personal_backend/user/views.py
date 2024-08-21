from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import permissions,generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token as AuthToken
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication


class UserRegistrationView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = AuthToken.objects.get_or_create(user=user)
            return Response({'Token': token.key})
        else:
            return Response(serializer.errors, status=400) 
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        user = authenticate(username=request.data['username'],password=request.data['password'])
        if user:
            token,created = AuthToken.objects.get_or_create(user=user)
            return Response({'Token':token.key})
        else:
            return Response({'error':'Invalid username or password'})

class UserTestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        print(request.META)
        print(request.user)
        return Response({'message':'Hello, you are authenticated'})
user_registration_view = UserRegistrationView.as_view()
user_login_view = UserLoginView.as_view()
user_test_view = UserTestAPI.as_view()
