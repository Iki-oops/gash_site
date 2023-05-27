from rest_framework.permissions import BasePermission, SAFE_METHODS


class CurrentUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method == 'GET'


class AnonUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous
