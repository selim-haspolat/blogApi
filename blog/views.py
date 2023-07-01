from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin
from .serializers import (
    Comment, CommentSerializer,
    Blog, BlogSerializer,
    Like, LikeSerializer,
    Category, CategorySerializer,
    PostView
)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get(self.lookup_field)
        if not PostView.objects.filter(user=request.user, post= id).exists():
            post_view = PostView(user=request.user, post_id=id)  
            post_view.save()  

        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LikeCreate(CreateModelMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    
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