from rest_framework import permissions


class CreateArtistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if not request.user.is_authenticated:
            return False
        return True
