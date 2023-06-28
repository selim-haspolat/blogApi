from django.urls import path, include

urlpatterns = [
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()

router.register('', UserViewSet)

urlpatterns += router.urls