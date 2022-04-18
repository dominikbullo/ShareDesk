from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        super(IsAdminOrReadOnly, self).has_permission(request, view)
        try:
            return request.user.is_administrator()
        except AttributeError as e:
            return False
