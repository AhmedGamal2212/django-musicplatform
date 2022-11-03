from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumViewSet.as_view({'get': 'list'})),
]
