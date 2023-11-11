from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreateUserAllowedOrReadOnly(BasePermission):
    """
    Renvoi True si la requête est de type GET, HEAD ou OPTIONS.
    L'utilisateur authentifié ne peut modifier ou supprimer  que ses données.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        print(request.method, obj.id, request.user.id)

        if request.method in SAFE_METHODS: # or request.user.is_authenticated:
            return True
        return obj.id == request.user.id



        # if request.method == "POST":  # or request.user.is_authenticated:
        #     return True
        # elif request.method == "PATCH": #and obj.username == request.user:
        #     return True
        # else:
        #     return False

    # def has_object_permission(self, request, view, obj):
    #     if request.method == "POST" or request.user.is_authenticated:
    #         if obj.id != request.user:
    #             return False
    #         return True
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     if obj.id == request.user:
    #         return True
    #     return False