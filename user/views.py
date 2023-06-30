from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import (User, UserSerializer)
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny

class CreateUserViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.fields['password'].required = True  # Password should be required for registration 
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        token = Token.objects.create(user=user)
        data = {'user': serializer.data, 'key': token.key}
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


