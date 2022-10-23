from django import forms
from .models import Album


class DateInput(forms.DateInput):
    input_type = 'date'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'release_date', 'cost', 'is_approved')
        help_texts = {
            'is_approved': 'Approve the album if its name is not explicit'
        }
        widgets = {
            'release_date': DateInput
        }
