from rest_framework import generics
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArtistAPIView(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
