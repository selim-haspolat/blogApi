from rest_framework import serializers
from .models import (
    Blog,
    Category,
    Comment
)

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        exclude = []

class BlogSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            'title',
            'content',
            'image' ,
            'category' ,
            'publish_date' ,
            'author' ,
            'status',
            'comments',
    ]

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data