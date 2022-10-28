from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistAPIView.as_view()),
]
