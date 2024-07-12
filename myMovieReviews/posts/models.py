from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(default=2000)
    genre = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    runtime = models.IntegerField(default=0)
    review = models.TextField()
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()