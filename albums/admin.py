from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'release time')


admin.site.register(Album, AlbumAdmin)
