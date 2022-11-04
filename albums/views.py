import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import Album
from .filters import AlbumFilter
from .pagination import CustomPagination


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


def check_params(query_param):
    if any(not (c.isdigit() or c == '-') for c in str(query_param)):
        raise ValidationError({
            'details': 'Cost and limit queries must be only numbers.'
        })


class AlbumViewSetManually(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(is_approved=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    paginate_by = 5

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name', '')
        cost_upper_bound = request.GET.get('cost__lte', (1 << 32))
        cost_lower_bound = request.GET.get('cost__gte', -(1 << 32))
        limit = request.GET.get('limit', 5)

        if limit is not None:
            check_params(str(limit))

        if cost_lower_bound is not None:
            check_params(str(cost_lower_bound))
            cost_lower_bound = float(cost_lower_bound)

        if cost_upper_bound is not None:
            check_params(str(cost_upper_bound))
            cost_upper_bound = float(cost_upper_bound)

        filtered = self.get_queryset().filter(name__icontains=name).filter(cost__lte=cost_upper_bound).filter(
            cost__gte=cost_lower_bound)
        paginated = self.paginate_queryset(filtered)
        serialized = self.get_serializer(paginated, many=True).data
        return self.get_paginated_response(serialized)
