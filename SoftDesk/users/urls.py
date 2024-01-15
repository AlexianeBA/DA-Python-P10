from rest_framework import routers
from .views import UserViewSet, ContributorViewSet
from Project.views import ProjectViewSet
router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('project', ProjectViewSet)
router.register('contributor', ContributorViewSet)