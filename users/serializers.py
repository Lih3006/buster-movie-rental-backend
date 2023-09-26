from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=127)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    
    def validate_username(self, value: str):
        all_users = User.objects.all()
        if all_users.filter(username=value).exists():
            raise serializers.ValidationError("username already taken.")
        return value
        
    def validate_email(self, value: str):
        all_users = User.objects.all()
        if all_users.filter(email=value).exists():
            raise serializers.ValidationError("email already registered.")
        return value
    
    def create(self, validated_data: dict):
        confirm_employee = validated_data['is_employee']
        
        if confirm_employee:
            validated_data.update({
                'is_employee': True,
                'is_superuser': True,
                'is_staff': True
            })
        else:
            validated_data.update({
                'is_employee': False,
                'is_superuser': False,
                'is_staff': False
            })
        validated_data['password'] = make_password(validated_data['password'])

        return User.objects.create(**validated_data)

    def update(self, instance: User, validated_data: dict):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = make_password(validated_data.get("password", instance.password))
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.is_employee = validated_data.get("is_employee", instance.is_employee)
        
        
        instance.save()
        
        return instance        
        
        
class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token
    
