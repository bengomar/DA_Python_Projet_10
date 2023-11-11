from rest_framework.permissions import BasePermission

from .models import Contributor, Issue


class IsContributor(BasePermission):
    """
    Vérifie si l'utilisateur connecté est contributeur sur le projet
    """

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(project=obj, user=request.user).exists()


class IsIssueContributor(BasePermission):
    """
    Vérifie si l'utilisateur connecté est contributeur sur le projet de l'issue
    """

    # Verifier si je suis contributeur d'un projet pour une issue précise
    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(
            project=obj.project, user=request.user
        ).exists()


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Si la requète est de type PUT, PATCH ou DELETE
        renvoie True si l'utilisateur connecté est l'auteur de l'objet
        """
        if request.method in ["PUT", "PATCH", "DELETE"]:
            if obj.author == request.user:
                return True
            return False
        return True


class IsProjetContributor(BasePermission):
    """
    Vérifie si l'utilisateur connecté est contributeur sur le projet
    """

    # Doit etre contributeur du projet
    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(project=obj, user=request.user).exists()
