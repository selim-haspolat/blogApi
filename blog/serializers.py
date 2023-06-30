from rest_framework import serializers
from .models import (
    Blog,
    Comment,
    Category,
    Like,
)


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        exclude = []


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        exclude = []


class BlogSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    likes_n = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        exclude = []

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data
    
    def get_comment_count(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        return len(comments)
    
    def get_likes_n(self, obj):
        likes = Like.objects.filter(post=obj.id)
        serializer = LikeSerializer(likes, many=True)
        return serializer.data
    
    def get_likes(self, obj):
        likes = Like.objects.filter(post=obj.id)
        return len(likes)