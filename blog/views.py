from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# create Tag Serializer
class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# create Post Serializer
class PostView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer
