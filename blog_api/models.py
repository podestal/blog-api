from django.db import models
from django.conf import settings

class Topic(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, blank=True)
    member_since = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}' 

class Post(models.Model):

    STATUS_IN_PROGRESS = 'P'
    STATUS_COMPLETED = 'C'

    STATUS_CHOICES = [
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
    ]

    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_IN_PROGRESS)
    # comment

    def __str__(self):
        return self.title

class Section(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Body(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="bodies")
    image = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=255, blank=True)

