from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    path = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.FileField(null=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
