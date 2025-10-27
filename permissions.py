from rest_framework.permissions import BasePermissionm, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated()
            )
            or
            (request.user and request.user.is_staff)
        )
