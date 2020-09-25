from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.PostList.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>/', views.TagDetail.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('myposts/', views.MyPosts.as_view()),
    path('myposts/<int:pk>', views.MyPostsDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]