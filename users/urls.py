from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersAPIView.as_view()),
    path('<int:pk>/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    })
         ),
]
