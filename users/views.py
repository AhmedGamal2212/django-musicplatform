from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
