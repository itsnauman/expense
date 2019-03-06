from django.urls import path
from expense import views

urlpatterns = [
    path('users/', views.UserViewset.as_view(), name='users'),
    path('users/<pk>/', views.UserDetail.as_view(), name='show_user'),
]
