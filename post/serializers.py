from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
import os
import base64
from django.conf import settings


"""
Tag serializers used for GET and PUSH requests.
"""
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name')
        model = models.Tag

"""
User serializers for registering users.
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


"""
Post serializers used to handle encoding image data and tags for name
Used for GET and PUSH requests
"""
class PostSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField('encode_image')

    tags = serializers.SerializerMethodField('get_tags')

    def encode_image(self, post):
        with open(os.path.join(settings.MEDIA_ROOT, post.image.name), "rb") as image_file:
            return base64.b64encode(image_file.read())

    def get_tags(self, post):
        try:
            post_tags = models.Tag.objects.filter(post__id = post.id)
            return TagSerializer(post_tags, many= True).data
        except:
            return None 
    class Meta:
        fields = ('id', 'message','tags','images','image')
        model = models.Post

