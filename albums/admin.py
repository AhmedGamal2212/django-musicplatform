from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'creation_date', 'release_date', 'is_approved')


admin.site.register(Album, AlbumAdmin)
