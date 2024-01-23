from rest_framework import permissions


class IsAuthorOfProject(permissions.BasePermission):
    message = "L'auteur du projet est le seul à pouvoir actualiser ce projet."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsContributorOFproject(permissions.BasePermission):
    message = "Vous n'êtes pas autorisé à modifier ce projet."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.contributor == request.user
