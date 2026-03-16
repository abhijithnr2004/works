from rest_framework.permissions import BasePermission

class IsAdminOwner(BasePermission):

    def has_permission(self, request, view):

        # Only admins can access
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        
        # Only the admin who created the customer can modify it
        return obj.owner == request.user