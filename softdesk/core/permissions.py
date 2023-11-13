from rest_framework.permissions import BasePermission

from .models import Contributor


class IsProjectContributor(BasePermission):
    """
    Vérifie si l'utilisateur connecté est contributeur sur le projet
    """

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(project=obj, user=request.user).exists()


class IsProjectContributorRelatedIssue(BasePermission):
    """
    Vérifie si l'utilisateur connecté est contributeur sur le projet de l'issue
    pour pouvoir accéder aux détails de l'issue
    """

    def has_object_permission(self, request, view, obj):
        print("IsIssueContributor exists ----->", obj.project, request.user)
        return Contributor.objects.filter(
            project=obj.project, user=request.user
        ).exists()


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        renvoie True si l'utilisateur connecté est l'auteur de l'objet
        """
        if obj.author.id == request.user.id:
            return True
        return False
