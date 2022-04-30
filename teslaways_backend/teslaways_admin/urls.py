from django.template import base
from django.urls import path, include
from .views import managezone_viewsets, managepodtip_viewsets, managenew_viewsets, managedestination_viewsets, managegallery_viewsets, admin_user_viewsets
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('zones', managezone_viewsets.ZoneViewSet, basename='zone')
router.register('podTips', managepodtip_viewsets.PodTipViewSet, basename='podtip')
router.register('news', managenew_viewsets.NewsViewSet, basename='news')
router.register('galleries', managegallery_viewsets.GalleryViewSet, basename='gallery')
router.register('destinations', managedestination_viewsets.DestinationViewSet, basename='destination')
router.register('admin_user', admin_user_viewsets.AdminUserViewSet, basename='admin_user')
router.register('admin_user/login', admin_user_viewsets.AdminUserViewSet, basename='admin_user')

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls))
]