from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from rest_framework import generics


class LoginAPI(generics.GenericAPIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)

        return Response({
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'bio': user.bio,
            },
        })


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            'token': token,
            'user': {
                'username': user.username,
                'email': user.email,
                'bio': user.bio
            }
        })
