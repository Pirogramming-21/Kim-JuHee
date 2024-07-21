from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=32)
    user=models.CharField(max_length=20)
    content=models.TextField()
    image_url = models.URLField(default='https://example.com/default-image.jpg')
    like = models.PositiveIntegerField(default=0)
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()