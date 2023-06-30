from django.urls import path
from .views import (
    BlogViewSet,
    CommentViewSet,
)


urlpatterns = [
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, CreateUserViewSet

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('comments', CommentViewSet)
# router.register('', UserViewSet)

urlpatterns += router.urls