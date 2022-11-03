from rest_framework import viewsets
from .serializers import AlbumSerializer
from .models import Album


# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(is_approved=True)
