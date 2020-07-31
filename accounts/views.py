from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (LoginRequiredMixin,
										UserPassesTestMixin,

	)
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (ListView, DetailView, 
								  CreateView, DeleteView
	)
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


from .models import *

# Create your views here.
from .forms import (CreateUserForm, UserUpdateForm, 
					ProfileUpdateForm, EditProfileForm,
					PostForm
)


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
	#profile = Profile.objects.get(id=pk)
	user_form = UserUpdateForm(request.POST, instance=request.user)
	profile_form = ProfileUpdateForm(request.POST, 
									request.FILES, 
									instance=request.user.profile)
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, 
										request.FILES, 
										instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Your account has been updated !')
			return redirect('accounts-user')
	
	context = {'user_form':user_form, 'profile_form':profile_form}
	return render(request, 'accounts/user.html', context)

def edit_profile(request):
	if request.method == 'POST':
		editpro_form = EditProfileForm(request.POST, 
									   request.FILES, 
									   instance=request.user.profile
		)
		user_form = UserUpdateForm(request.POST, instance=request.user)

		if editpro_form.is_valid(): #user_form.is_valid()
			#user_form.save()
			editpro_form.save()
			messages.success(request, f'Your account has been updated!')
			print('updated')
			return redirect('accounts-user')

	else:
		editpro_form = EditProfileForm(instance=request.user.profile)
		user_form = UserUpdateForm(instance=request.user)


	context = {'editpro_form': editpro_form, 'user_form':user_form }
	return render(request, 'accounts/edit_profile.html', context)


def logoutUser(request):
	logout(request)
	return redirect('accounts-login')


def home(request):
	form = PostForm()
	posts = Post.objects.all()

	if form.is_valid(): 
		form.save()
		messages.success(request, f'Post created!')
		print('created')
		return redirect('accounts-home')

	context = {'posts': posts, 'form':form}
	return render(request, 'accounts/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'accounts/home.html'
	context_object_name = 'posts'
	ordering = ['-date_created']
	paginate_by = 2

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['content']
	success_url = '/'
	
	def form_valid(self, form):
		form.instance.blogger = self.request.user
		return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.blogger:
			return True
		return False

class UserPostListView(ListView):
	model = Post
	template_name = 'accounts/user_posts.html'
	context_object_name = 'posts'
	#ordering = ['-date_created']
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(blogger=user).order_by('-date_created')


#comments
class CommentListView(ListView):
	model = Comment
	template_name = 'accounts/comments.html'
	context_object_name = 'comments'
	#ordering = ['-date_created']
	#paginate_by = 2


def about(request):
	return render(request, 'accounts/about.html')
