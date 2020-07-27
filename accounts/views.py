from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


from .models import *

# Create your views here.
from .forms import CreateUserForm


def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('accounts-login')

	context = {'form': form}
	return render(request, 'accounts/register.html', context)


def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('accounts-home')

		else:
			messages.info(request, f'Username OR Password is incorrect')
			return render(request, 'accounts/login.html')

	context = {}
	return render(request, 'accounts/login.html', context)

def user(request):
	
	context = {}
	return render(request, 'accounts/user.html', context)


def logoutUser(request):
	logout(request)
	return redirect('accounts-login')


def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'accounts/home.html', context)


def about(request):
	return render(request, 'accounts/about.html')
