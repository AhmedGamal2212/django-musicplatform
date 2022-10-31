from rest_framework.response import Response
from .permissions import EditPermission
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class UsersAPIView(APIView):
    def get(self, request):
        return Response(UserSerializer(CustomUser.objects.all(), many=True).data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, EditPermission]
    queryset = CustomUser.objects.all()
