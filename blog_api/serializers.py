from rest_framework import serializers
from core.serializers import GetUserSerializer
from . import models

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ['id', 'created_at', 'title']

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Body
        fields = ['id', 'image', 'code', 'text', 'section']

class CreateBodySeralizer(serializers.ModelSerializer):
    class Meta:
        model = models.Body
        fields = ['image', 'code', 'text']
    
    def save(self, **kwargs):
        section_id = self.context['section_id']
        return models.Body.objects.create(section_id = section_id, **self.validated_data)

class SectionSerializer(serializers.ModelSerializer):

    bodies = BodySerializer(many=True)

    class Meta:
        model = models.Section
        fields = ['id', 'title', 'post', 'bodies']

class CreateSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        fields = ['title']

    def save(self, **kwargs):
        post_id = self.context['post_id']
        return models.Section.objects.create(post_id = post_id, **self.validated_data)

class PostSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = models.Post
        fields = ['id', 'created_at', 'title', 'status', 'author', 'topic', 'sections']

class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'topic']

    def save(self, **kwargs):
        print(self)
        user_id = self.context['user_id']
        author = models.Author.objects.get(user_id=user_id)
        return models.Post.objects.create(author_id=author.id, **self.validated_data)


class AuthorSerializer(serializers.ModelSerializer):

    user = GetUserSerializer()

    class Meta:
        model = models.Author
        fields = ['id', 'job_title', 'member_since', 'user']

class CreateAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = ['job_title', 'user']
