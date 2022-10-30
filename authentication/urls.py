from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_api),
    path('login/', views.login_api),
]
