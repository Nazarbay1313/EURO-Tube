from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CommentModelViewSet, FavoriteModelViewSet,
                       ProductModelViewSet, UserModelViewSet)

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'favorites', FavoriteModelViewSet)
router.register(r'comments', CommentModelViewSet)
router.register(r'users', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
