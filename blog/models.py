from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="blog/photos",
                              default="/blog/default.jpg")
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    vip_content = models.BooleanField(default=False)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True)

    class Meta():
        ordering = ['created_at']

    def __ster__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('blog:single', kwargs={"pid": self.id})
