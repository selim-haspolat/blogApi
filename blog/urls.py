from django.urls import path
from .views import (
    BlogViewSet,
    CommentViewSet,
    LikeCreate,
)

urlpatterns = [
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, CreateUserViewSet

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('comments', CommentViewSet)
router.register('like', LikeCreate)

urlpatterns += router.urls