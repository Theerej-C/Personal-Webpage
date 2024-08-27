from rest_framework import serializers
from  .models import CustomUser 
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','password','is_active','phone_number']
    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    def update(self,instance,validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super.update(instance,validated_data)