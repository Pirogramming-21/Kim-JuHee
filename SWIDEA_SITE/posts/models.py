from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=2000, default="https://media.istockphoto.com/id/1396814518/vector…20&c=hnh2OZgQGhf0b46-J2z7aHbIWwq8HNlSDaNp2wn_iko=")
    review = models.TextField()
    rating = models.FloatField(default=0.0)
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, null=True, blank=True) 
    
class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
    
