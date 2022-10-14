from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('stage name', 'email address')


# Register your models here.
admin.site.register(Artist, ArtistAdmin)
