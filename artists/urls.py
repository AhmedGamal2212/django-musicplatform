from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view()),
    path('create/', views.ArtistFormView.as_view())
]
