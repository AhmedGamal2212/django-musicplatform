from rest_framework import generics
from .models import Artist
from .serializers import ArtistSerializer


class ArtistAPIView(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
