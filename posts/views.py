from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def blog_posts(request):
    # Fetch blog posts and render them using blog template
    pass

def philosophy_posts(request):
    # Fetch philosophy posts and render them using philosophy template
    pass

def reviews_posts(request):
    # Fetch reviews posts and render them using reviews template
    pass

def science_posts(request):
    # Fetch science posts and render them using science template
    pass

def wildlife_posts(request):
    # Fetch wildlife posts and render them using wildlife template
    pass

def post_detail(request, category, id):         ## Allows individual posts to be directly requested and displayed
    # Fetch the post by id and render it using the appropriate template based on category
    pass