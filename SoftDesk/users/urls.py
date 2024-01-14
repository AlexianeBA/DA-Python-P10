from rest_framework import routers
from .views import UserViewSet, ProjectViewSet
router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('project', ProjectViewSet)