from django.db import models
from django.contrib.auth.models import User
#from django.DateTimeField import DateTimeField

# Create your models here.
class Role(models.Model):

	ROLES =  (
		('Admin', 'Admin'),
		('User', 'User'),
		)

	name = models.CharField(max_length=200, null=True, choices=ROLES)
	default_role = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name

class Blogger(models.Model):
	role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="default.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True,null=True)
	blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

	def __str__(self):
		return self.id


class Comment(models.Model):
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.ManyToManyField(Post, null=True, blank=True, on_delete=models.CASCADE)
	blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

	def __str__(self):
		return self.id
		