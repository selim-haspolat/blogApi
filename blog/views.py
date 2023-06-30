from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Comment, CommentSerializer,
    Blog, BlogSerializer
)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer