from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]


# --------------- Router ---------------

from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()

router.register('', UserViewSet)

urlpatterns += router.urls