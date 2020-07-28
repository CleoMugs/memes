from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='accounts-home'),
    path('about/', views.about, name='accounts-about'),


    path('register/', views.register, name='accounts-register'),
    path('login/', views.loginPage, name='accounts-login'),
    path('logout/', views.logoutUser, name='accounts-logout'),

    path('user/', views.user, name='accounts-user'),
    path('edit-profile/', views.edit_profile, name='accounts-editprofile'),
    
]