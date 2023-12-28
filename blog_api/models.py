from django.db import models
from django.conf import settings

class Topic(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    member_since = models.DateTimeField(auto_now=True)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    # comment

class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)

class Body(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="bodies")
    image = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=255, blank=True)

