from django.contrib import admin
from .models import Album, Song
from .forms import AlbumForm


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'created', 'release_date', 'cost', 'is_approved')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
