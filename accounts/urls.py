from django.urls import path
from .views import (PostListView, PostDetailView, 
					PostCreateView, PostDeleteView,
					UserPostListView
					)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='accounts-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='accounts-about'),


    path('register/', views.register, name='accounts-register'),
    path('login/', views.loginPage, name='accounts-login'),
    path('logout/', views.logoutUser, name='accounts-logout'),

    #path('user/', views.user, name='accounts-user'),
    path('edit-profile/', views.edit_profile, name='accounts-editprofile'),
    
]