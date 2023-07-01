from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .permissions import IsAdminOrReadOnly
from .serializers import (
    Comment, CommentSerializer,
    Blog, BlogSerializer,
    Like, LikeSerializer,
    Category, CategorySerializer,
    PostView,
)


class CommentView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        from rest_framework.response import Response
        from rest_framework import status

        request.data['post'] = self.kwargs.get('pk')
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        from rest_framework.response import Response
        from rest_framework import status

        comments = Comment.objects.filter(post=self.kwargs.get('pk'))
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['author'] = request.user
 
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get(self.lookup_field)
        if not PostView.objects.filter(user=request.user, post= id).exists():
            post_view = PostView(user=request.user, post_id=id)  
            post_view.save()  

        return super().retrieve(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]


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