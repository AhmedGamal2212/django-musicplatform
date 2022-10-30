from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersAPIView.as_view()),
    path('<int:pk>/', views.UserAPIView.as_view()),
]
