from django.db import models
from django.utils import timezone

# Create your models here.

class Memo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos')
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=timezone.now)