from rest_framework.viewsets import ModelViewSet
from .serializers import (User, UserSerializer)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer