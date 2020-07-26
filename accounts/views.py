from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Create your views here.


def register(request):
	form = UserCreationForm()
	context = {'form': form}
	return render(request, 'accounts/register.html', context)


def login(request):
	form = UserCreationForm()
	context = {'form': form}
	return render(request, 'accounts/login.html', context)


def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'accounts/home.html', context)


def about(request):
	return render(request, 'accounts/about.html')
