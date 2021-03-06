from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	profile_pic = models.ImageField(default="default.png", upload_to='images')
	location =  models.CharField(max_length=200, null=True, blank=True)
	occupation =  models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return f'{self.user.username} Profile'


class Role(models.Model):

	ROLES =  (
		('Admin', 'Admin'),
		('User', 'User'),
		)

	name = models.CharField(max_length=200, null=True, default='User', choices=ROLES)
	#default_role = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.name)

class Post(models.Model):
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	blogger = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)

	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})
	

class Comment(models.Model):
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	blogger = models.ForeignKey(User, on_delete=models.CASCADE)


	class Meta:
		ordering = ['-date_created']


	def __str__(self):
		return str(self.id)
