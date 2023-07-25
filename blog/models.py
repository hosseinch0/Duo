from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    image = models.ImageField(upload_to="blog", default="/blog/default.jpg")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['created_at']


    def __ster__(self):
        return self.title