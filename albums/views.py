import math

import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import Album
from .filters import AlbumFilter


# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(is_approved=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = AlbumFilter

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


class AlbumViewSetManually(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(is_approved=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def list(self, request, *args, **kwargs):
        name = request.query_params.get('name', '')
        cost_upper_bound = request.GET.get('cost__lte', (1 << 32))
        cost_lower_bound = request.GET.get('cost__gte', -(1 << 32))

        if cost_lower_bound is not None:
            if any(not(c.isdigit() or c == '-') for c in str(cost_lower_bound)):
                print(cost_lower_bound)
                raise ValidationError('Cost queries must be only numbers.')
            cost_lower_bound = float(cost_lower_bound)

        if cost_upper_bound is not None:
            if any(not(c.isdigit() or c == '-') for c in str(cost_upper_bound)):
                print(cost_upper_bound)
                raise ValidationError('Cost queries must be only numbers.')
            cost_upper_bound = float(cost_upper_bound)

        filtered = self.get_queryset().filter(name__icontains=name).filter(cost__lte=cost_upper_bound).filter(cost__gte=cost_lower_bound)
        return Response(AlbumSerializer(filtered, many=True).data)
