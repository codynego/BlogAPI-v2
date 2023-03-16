from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	category = CategorySerializer()
	class Meta:
		model = Post
		fields = ('id', 'author', 'title', 'body', 'created_date', 'modified_date', 'category')

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	class Meta:
		model = Comment
		fields = ('id', 'post', 'author', 'body', 'created_date', 'modified_date')