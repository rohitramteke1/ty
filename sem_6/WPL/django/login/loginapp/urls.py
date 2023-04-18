from django.urls import path, include
from loginapp import views

urlpatterns = [
    path('home/', views.loginapp, name='loginapp'),
]