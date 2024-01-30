"""
URL configuration for SoftDesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from issue.views import IssueViewSets
from comment.views import CommentViewSets
from Project.views import ProjectViewSet
from users.views import UserViewSet, ContributorProjectViewSet

user_router = routers.DefaultRouter()
user_router.register("user", UserViewSet)
user_router.register("contributor-project", ContributorProjectViewSet)

project_router = routers.DefaultRouter()
project_router.register("project", ProjectViewSet)

comment_router = routers.DefaultRouter()
comment_router.register("comment", CommentViewSets)


issue_router = routers.DefaultRouter()
issue_router.register("issue", IssueViewSets)


router = routers.DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(project_router.registry)
router.registry.extend(comment_router.registry)
router.registry.extend(issue_router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router.urls)),
]
