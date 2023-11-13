from rest_framework.permissions import SAFE_METHODS, BasePermission


class CreateUserAllowedOrReadOnly(BasePermission):
    """
    Renvoi True si la requête est de type GET, HEAD ou OPTIONS.
    L'utilisateur authentifié ne peut modifier ou supprimer  que ses données.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id
