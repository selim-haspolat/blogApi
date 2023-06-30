from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .serializers import (
    Comment, CommentSerializer,
    Blog, BlogSerializer,
    Like, LikeSerializer
)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class LikeCreate(CreateModelMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')
        post = request.data.get('post')
        
        if Like.objects.filter(user=user, post=post):
            from rest_framework.response import Response
            from rest_framework import status

            like = Like.objects.get(user=user, post=post)
            like.delete()
            like_data = LikeSerializer(like) #! id null dönüyor
            return Response(like_data.data, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)