from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class TopicViewSet(ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer

class SectionViewSet(ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer

class BodyViewSet(ModelViewSet):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer

class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


