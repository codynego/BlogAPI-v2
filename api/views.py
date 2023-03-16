from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Post, Comment 
from .serializers import CategorySerializer, PostSerializer, CommentSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
	search_fields = ('title', 'body', 'author__username', 'category__name')
	ordering_fields = '__all__'
	filterset_fields = {
    'category': ['exact'],
    'category__name': ['exact'],
    'category__id': ['exact'],
}

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class Categories(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class Comments(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
