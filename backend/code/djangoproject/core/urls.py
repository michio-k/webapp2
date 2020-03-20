from django.urls import path
from django.conf.urls import url
from rest_framework import routers

# from .views import UserViewSet
# from .views import PostViewSet
from .views import auth0_views
from .views import AppUserViewSet

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)
router.register(r'appusers', AppUserViewSet)

urlpatterns = [
    path('api/public', auth0_views.public),
    path('api/private', auth0_views.private),
    path('api/private-scoped', auth0_views.private_scoped),
]
