from django.urls import path
from .views import (
    BlogViewSet,
    LikeCreate,
    CategoryViewSet,
    CommentView
)

urlpatterns = [
    path('comments/<int:pk>', CommentView.as_view()),
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('likes', LikeCreate)
router.register('categories', CategoryViewSet)

urlpatterns += router.urls