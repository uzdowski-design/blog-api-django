from rest_framework import serializers
from .models import Tag, Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'url')


# create Tag serializer (JSON data reprezentation)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'url')


# create Post serializer (JSON data reprezentation)
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'abstract',
                  'body', 'created_date', 'author', 'tags')
