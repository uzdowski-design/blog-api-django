from rest_framework import serializers
from .models import Tag, Post


# create Tag serializer (JSON data reprezentation)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


# create Post serializer (JSON data reprezentation)
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'abstract',
                  'body', 'created_date', 'author', 'tags')
