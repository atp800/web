from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field

STATUS_CHOICES = (
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published'),
    ('DELETED', 'Deleted'),
)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = CKEditor5Field(blank=True, null=True, config_name='extends')#RichTextUploadingField(blank=True, null=True)
    section = models.CharField(max_length=50, null=True, blank=True)
    topic = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=300, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title