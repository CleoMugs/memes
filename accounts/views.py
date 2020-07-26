from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.

posts = [
	{
		'blogger': 'Cleo',
		'content': 'First post',
		'date_created': 'July 26, 2020'
	},

	{
		'blogger': 'Mugs',
		'content': 'Second post',
		'date_created': 'July 25, 2020'
	}
]


def home(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request, 'accounts/home.html', context)


def about(request):
	return render(request, 'accounts/about.html')
