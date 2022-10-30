from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView


class UsersAPIView(APIView):
    def get(self, request):
        return Response(UserSerializer(CustomUser.objects.all(), many=True).data)


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        data = request.data

        user.username = data['username']
        user.bio = data['bio']
        user.email = data['email']
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        data = request.data

        user.username = data.get('username', user.username)
        user.bio = data.get('bio', user.bio)
        user.email = data.get('email', user.email)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)
