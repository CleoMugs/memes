from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUserForm(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):	
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic', 'location', 'occupation']

class EditProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['location', 'occupation', 'profile_pic']

		model = User
		fields = ['first_name', 'last_name']

