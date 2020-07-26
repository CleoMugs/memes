from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import *

# Create your views here.
from .forms import CreateUserForm


def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			#form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('accounts-login')

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
