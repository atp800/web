from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_posts, name='blog_posts'),
    path('philosophy/', views.philosophy_posts, name='philosophy_posts'),
    path('reviews/', views.reviews_posts, name='reviews_posts'),
    path('science/', views.science_posts, name='science_posts'),
    path('wildlife/', views.wildlife_posts, name='wildlife_posts'),
    path('<str:category>/<int:id>/', views.post_detail, name='post_detail'),
]