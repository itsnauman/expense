from django.urls import path
from expense import views

urlpatterns = [
    path('users/', views.UserViewset.as_view(), name='users'),
    path('auth/signup/', views.CreateAccountView.as_view(), name='signup')
]
