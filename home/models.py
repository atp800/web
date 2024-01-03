from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)