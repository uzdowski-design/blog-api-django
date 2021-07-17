from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer


# create Tag Serializer
class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# create Post Serializer
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
