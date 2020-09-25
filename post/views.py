from django.shortcuts import render
from rest_framework import generics
from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
# Create your views here.


"""
Post view for the GET and POST requests
"""
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        post_save = PostSerializer(data=request.data)
        if post_save.is_valid():
            post_save.save()
            return Response(post_save.data)
        else:
            return Response(post_save.errors)


"""
Tag View for the GET and POST request on the Tag Model for the authenticated users only
"""  
class TagList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


"""
Tag detail view only for the authenticated users only
"""
class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


"""
Posts for the current user access using the either Token generated using the registering user first
Then with the http://127.0.0.1/api/api-token-auth/ with the username="" and password="" parameter 
"""
class MyPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user)

"""
Post Detail for the current user only
"""
class MyPostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all().filter(user=user)
  
"""
Post detail view for authenticated users only
"""
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
  
"""
Registering view
"""
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )