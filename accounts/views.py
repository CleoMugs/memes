from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Create your views here.
from .forms import CreateUserForm


def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

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
