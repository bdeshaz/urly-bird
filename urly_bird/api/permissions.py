from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.creator  # TODO: ADDING CREATOR COULD BE ISSUE. UPDATED MODEL


class OwnsRelatedContact(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.api.creator  # TODO: ADDING CREATOR COULD BE ISSUE
