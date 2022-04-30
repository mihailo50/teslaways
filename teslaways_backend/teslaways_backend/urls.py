from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teslaways.urls')),
    path('teslaways_admin/', include('teslaways_admin.urls')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)