# accounts/serializers.py

from rest_framework import serializers
from .models import User, RoleMaster
from rest_framework.authtoken.models import Token

class RoleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'password', 'confirm_password', 'gender', 'role', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'default': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()

         # Create a token for the user
        # Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
