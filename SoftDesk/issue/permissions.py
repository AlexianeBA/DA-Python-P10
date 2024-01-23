from rest_framework import permissions


class IsAuthorOfIssue(permissions.BasePermission):
    message = "L'auteur du problème est le seul à pouvoir actualiser ce commentaire."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsContributorOFIssue(permissions.BasePermission):
    message = "Vous n'êtes pas autorisé à modifier ce problème."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.contributor == request.user
