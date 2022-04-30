from rest_framework import viewsets
from teslaways_admin.serializers import admin_user_serializer
from teslaways.models import admin_user
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

class AdminUserViewSet(viewsets.ModelViewSet):

    queryset = admin_user.AdminUser.objects.all()
    serializer_class = admin_user_serializer.CreateAdminUserSerializer
    http_method_names = ['get', 'post', 'delete', 'put']

