from django.urls import path
from . import views

urlpatterns = [path('', views.home, name= 'Home'),
               path('signup/', views.sign_up, name= 'SignUp')]
