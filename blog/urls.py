from django.urls import path
from .views import (
    BlogViewSet,
    CommentViewSet,
    LikeCreate,
    CategoryViewSet,
)

urlpatterns = [
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeCreate)
router.register('categories', CategoryViewSet)

urlpatterns += router.urls