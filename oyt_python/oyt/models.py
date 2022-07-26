# Copyright 2021 Bhargav SNV
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    path = models.CharField(max_length=1000)
    img_path = models.CharField(max_length=1000, null=True)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.FileField(null=True)
    is_private = models.BooleanField(default=False)
    likes = models.JSONField()
    num_likes = models.IntegerField(default=0)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, null=True)


class Images(models.Model):
    img_path = models.CharField(max_length=1000, null=True)
    img = models.FileField(null=True)
    id = models.AutoField(primary_key=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    is_private = models.BooleanField(default=False)
    description = models.CharField(max_length=300, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video_ids = models.JSONField()


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100, null=False)
