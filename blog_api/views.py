from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers

class PostViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreatePostSerializer
        elif self.request.method == 'PATCH':
            return serializers.EditPostSerializer
        return serializers.PostSerializer
    
    def get_queryset(self):
        (author, created) = models.Author.objects.get_or_create(user_id= self.request.user.id)
        return models.Post.objects.filter(author_id = author.id)
    
class AllPostsViewSet(ModelViewSet):
    queryset = models.Post.objects.filter(status='C')
    serializer_class = serializers.PostSerializer
    http_method_names = ['get']



class TopicViewSet(ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SectionViewSet(ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return models.Section.objects.select_related("post").filter(post_id = self.kwargs['posts_pk'])

    def get_serializer_context(self):
        return {"post_id": self.kwargs['posts_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateSectionSerializer
        return serializers.SectionSerializer

class BodyViewSet(ModelViewSet):

    queryset =  models.Body.objects.select_related('section').all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']

    # def get_queryset(self):
    #     return models.Body.objects.select_related('section').filter(section_id = self.kwargs['sections_pk'])

    def get_serializer_context(self):
        return {"section_id": self.kwargs['sections_pk']}
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateBodySeralizer
        return serializers.BodySerializer

class AuthorViewSet(ModelViewSet):

    serializer_class = serializers.AuthorSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_context(self):
        # posts = models.Post.objects.filter(author_id)
        return {"user_id": self.request.user.id}
    
    def get_queryset(self):
        return models.Author.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateAuthorSerializer
        return serializers.AuthorSerializer
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        author = models.Author.objects.get(user_id=self.request.user.id)
        serializer = serializers.AuthorSerializer(author)
        print(serializer.data)
        return Response(serializer.data)
    



