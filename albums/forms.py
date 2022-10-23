from django.forms import ModelForm
from .models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'release_date', 'is_approved')
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit'
        }
