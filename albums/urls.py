from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlbumList.as_view()),
]
