from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles",
                              default="profiles/black-cloud.png")
    description = models.TextField(max_length=255, null=True)

    def __str__(self):
        return f'{self.user.username}'


class Ticket(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
