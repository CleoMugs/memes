from django.urls import path
from django.contrib.auth import views as auth_views
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

    #path('post/<int:pk>/comments/', CommentListView.as_view(), name='post-comments'),

    path('comments/', views.comment, name='post-comments'),


    path('register/', views.register, name='accounts-register'),
    path('login/', views.loginPage, name='accounts-login'),
    path('logout/', views.logoutUser, name='accounts-logout'),

    #path('user/', views.user, name='accounts-user'),
    path('edit-profile/', views.edit_profile, name='accounts-editprofile'),



    path('reset_password/', 
    	auth_views.PasswordResetView.as_view(
    		template_name='accounts/password_reset.html'), 
    	name="reset_password" ),

    path('reset_password_sent/', 
    	auth_views.PasswordResetDoneView.as_view(
    		template_name='accounts/password_reset_sent.html'), 
    	name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    	auth_views.PasswordResetConfirmView.as_view(
    		template_name='accounts/password_reset_form.html'), 
    	name="password_reset_confirm"),

    path('reset_password_complete/', 
    	auth_views.PasswordResetCompleteView.as_view(
    		template_name='accounts/password_reset_complete.html'), 
    	name="password_reset_complete"),
    
]