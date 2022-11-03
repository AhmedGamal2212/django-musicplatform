from rest_framework import generics
from rest_framework.response import Response

from .models import Artist
from .serializers import ArtistSerializer
from .permissions import CreateArtistPermission


class ArtistAPIView(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    permission_classes = [CreateArtistPermission]

    def create(self, request, *args, **kwargs):
        if hasattr(request.user, 'artist'):
            return Response({
                'details': 'You are already an artist'
            }, status=403)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        artist = serializer.save(user=request.user)
        return Response({
            'id': artist.id,
            'stage_name': artist.stage_name,
            'social_link': artist.social_link
        })
