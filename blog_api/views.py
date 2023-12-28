from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from . import models
from . import serializers

class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreatePostSerializer
        return serializers.PostSerializer
    
    def get_queryset(self):
        (author_id, created) = models.Author.objects.only("id").get_or_create(user_id= self.request.user.id)
        return models.Post.objects.filter(author_id = author_id)


class TopicViewSet(ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    permission_classes = [IsAdminUser]

class SectionViewSet(ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return models.Section.objects.select_related("post").filter(post_id = self.kwargs['posts_id'])

    def get_serializer_context(self):
        return {"post_id": self.kwargs['posts_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateSectionSerializer
        return serializers.SectionSerializer

class BodyViewSet(ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return models.Body.objects.select_related('section').filter(section_id = self.kwargs['sections_pk'])

    def get_serializer_context(self):
        return {"section_id": self.kwargs['sections_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateBodySeralizer
        return serializers.BodySerializer

class AuthorViewSet(ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    
    def get_queryset(self):
        return models.Author.objects.filter(user_id=self.request.user.id)


