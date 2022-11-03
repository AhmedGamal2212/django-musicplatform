from django_filters import FilterSet, NumberFilter
from .models import Album


class AlbumFilter(FilterSet):
    class Meta:
        model = Album
        fields = {
            'name': [
                'icontains',
            ],
            'cost': [
                'lte',
                'gte',
            ]
        }
