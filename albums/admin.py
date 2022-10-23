from django.contrib import admin
from .models import Album
from .forms import AlbumForm


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'creation_date', 'release_date', 'is_approved')
    form = AlbumForm


admin.site.register(Album, AlbumAdmin)
