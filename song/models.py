from django.db import models
from django.conf import settings

# Create your models here.

class S_Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, default='이름을 입력해주세요')
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

class Song_comment(models.Model):
    def __str__(self):
        return self.text

    blog_id = models.ForeignKey(S_Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)