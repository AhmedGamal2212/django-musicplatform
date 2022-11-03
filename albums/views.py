from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import AlbumSerializer
from .models import Album


# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(is_approved=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        if not hasattr(request.user, 'artist'):
            return Response({
                'details': 'You should be an artist to create an album.'
            }, status=403)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        album_name = request.data['name']
        if request.user.artist.album_set.filter(name=album_name).count():
            return Response({
                'details': "You already have an album with the same name."
            }, status=400)
        serializer.save(artist=request.user.artist)
        return Response(serializer.data, status=200)
