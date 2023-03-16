from django.urls import path

from . import views

urlpatterns = [
    #path('api/', views.apiOverview, name='api-overview'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('comments/', views.Comments.as_view(), name='comments'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='commentdetail'),
]