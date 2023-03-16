from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
	
class Post (models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	
class Comment (models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	author = models.CharField(max_length=50)
	body = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body