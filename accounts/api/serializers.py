from rest_framework import serializers

from accounts.models import *

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Role
		fields = '__all__' 

'''
class BloggerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blogger
		fields = '__all__' 
'''

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__' 

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__' 
		