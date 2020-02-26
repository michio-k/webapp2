from django.urls import path
from rest_framework import routers

from .views import UserViewSet
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

# urlpatterns = [
#     path('', views.index, name='index'),
# ]