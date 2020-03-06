from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from .views import UserViewSet
from .views import PostViewSet
from .views import auth0_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    url(r'api/public', auth0_views.public),
    url(r'api/private', auth0_views.private),
    url(r'api/private-scoped', auth0_views.private_scoped),
]
