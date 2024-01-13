from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_data = {
        "title": post.title,
        "content": post.content,
        "image": post.image.url,
        "author": post.author,
        "section":post.section,
        "published": post.published_at,
        "updated": post.updated_at
    }
    return JsonResponse(post_data)


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