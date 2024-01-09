from django.conf import settings
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['post_id', 'title', 'slug', 'image', 'description', 'content', 'section', 'topic', 'tags', 'author', 
                  'views', 'status', 'created_at', 'updated_at', 'deleted_at', 'published_at']

    def get_image(self, post):
        if post.image:
            return 'http://localhost:8000' + settings.MEDIA_URL + str(post.image)
        return None