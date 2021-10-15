from django.db import models

# Create your models here.
class Gram(models.Model): #Blog
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100, default='name')
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class Gram_Comment(models.Model): #comment
    def __str__(self):
        return self.text

    blog_id = models.ForeignKey(Gram, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)