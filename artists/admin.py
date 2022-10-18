from django.contrib import admin
from .models import Artist
from albums.models import Album


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage_name', 'social_link')
    inlines = [AlbumInline]


# Register your models here.
admin.site.register(Artist, ArtistAdmin)
