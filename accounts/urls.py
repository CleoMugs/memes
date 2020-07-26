from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts-home'),
    path('about/', views.about, name='accounts-about'),
    path('register/', views.register, name='accounts-register'),
    path('login/', views.login, name='accounts-login'),
    
]