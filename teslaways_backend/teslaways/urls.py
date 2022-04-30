from django.urls import path, include
from teslaways.views import views_destination, views_news, view_baneri, view_staticki, view_slajder
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('news', views_news.NewsViewSet, basename='news')
router.register('destinations', views_destination.DestinationsViewSet, basename='destination')
router.register('maps', views_destination.MapViewSet, basename='podtip')
router.register('baneri', view_baneri.BaneriViewSet, basename='baneri')
router.register('slajderi', view_slajder.SlajderViewSet, basename='slajderi')
router.register('staticki', view_staticki.StatickiViewSet, basename='staticki')
router.register('news-zones', views_news.NewsZones, basename='news')
router.register('pocetna', views_news.PocetnaStranica, basename='news')
router.register('destinations-zones', views_destination.DestinatonsZones, basename='destinations')
router.register('destinations-podtips', views_destination.DestinatonsPodTip, basename='destinations_podtip')
router.register('destinations-tips', views_destination.DestinatonsTips, basename='destinations_tips')


urlpatterns = [
    path('', include(router.urls)),
]

