from django.conf import settings
from django.db import models
from django.utils import timezone

#모델을 정의하는 코드
class Post(models.Model):
    author = models.ForeignKey(settings.AUth_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_lenth=200)
    text = models.TimeField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
