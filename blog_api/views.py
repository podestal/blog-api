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

    def get_queryset(self):
        return models.Section.objects.filter(post_id = self.kwargs['posts_id'])

    def get_serializer_context(self):
        return {"post_id": self.kwargs['posts_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateSectionSerializer
        return serializers.SectionSerializer

class BodyViewSet(ModelViewSet):

    def get_queryset(self):
        return models.Body.objects.filter(section_id = self.kwargs['sections_pk'])

    def get_serializer_context(self):
        return {"section_id": self.kwargs['sections_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateBodySeralizer
        return serializers.BodySerializer

class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


