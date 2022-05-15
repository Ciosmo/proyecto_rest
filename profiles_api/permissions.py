from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        """Chequea si el user esta intentando editar su propio perfil"""

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Prmite actualizar propio status feed """
    def has_object_permission(self, request, view, obj):
        """Chequea si el user esta intentando editar su propio perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id
