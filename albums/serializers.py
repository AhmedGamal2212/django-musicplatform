from rest_framework import serializers, validators
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField('get_artist')

    def get_artist(self, obj):
        artist = obj.artist
        return {
            'id': artist.id,
            'stage_name': artist.stage_name,
            'social_link': artist.social_link
        }

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'cost', 'is_approved')
