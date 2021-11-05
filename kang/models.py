from django.db import models
from django.conf import settings
from django.urls import reverse

# CRUD
class KangBlog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    Blog_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Blog_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#댓글
class KangComment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(KangBlog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True) 