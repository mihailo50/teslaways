from django.contrib import admin

from .models import destination, gallery, news, podtip, zone, admin_user, baneri, staticki, slajder


admin.site.site_header = "Tesla Ways Admin Stranica"



@admin.register(zone.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)
    search_fields = ('id', 'name',)

@admin.register(podtip.Podtip)
class PodtipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'map_show')
    list_filter = ('name',)
    search_fields = ('id', 'name')


@admin.register(destination.Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'slug', 'created', 'updated', 'zone', 'pod_tip', 'tip')
    list_filter = ('created','title')
    search_fields = ('id', 'title')
    ordering = ('-created',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(news.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'created', 'updated', 'zone')
    list_filter = ('created','title')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('-created',)

@admin.register(gallery.DestinationGallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id',)

@admin.register(admin_user.AdminUser)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('id', 'username')

@admin.register(baneri.Banana)
class BaneriAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'active')
    search_fields = ('id',)

@admin.register(slajder.Slajder)
class SlajderAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'active')
    search_fields = ('id',)

@admin.register(staticki.Staticki)
class StatickiAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    search_fields = ('title','id')