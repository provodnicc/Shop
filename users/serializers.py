from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, label='Password')
    password2 = serializers.CharField(write_only=True, label='Confirm Password')

    def create(self, validated_data):
        if validated_data['password1'] and validated_data['password2'] and validated_data['password1'] != \
                validated_data['password2']:
            raise ValidationError('Passwords don`t match')

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password1']
        )
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')
        
            
