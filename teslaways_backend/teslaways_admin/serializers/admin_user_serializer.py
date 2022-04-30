from rest_framework import serializers
from teslaways.models import admin_user
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CreateAdminUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = admin_user.AdminUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = admin_user.AdminUser()
        password = validated_data['password']
        user.username = validated_data['username']
        user.password = user.create_hashed_password(password)
        user.save()
        return user


    def update(self, user, data):
        user.username = data['username']
        user.password = admin_user.AdminUser.create_hashed_password(self, data['password'])
        user.save()
        return user
        