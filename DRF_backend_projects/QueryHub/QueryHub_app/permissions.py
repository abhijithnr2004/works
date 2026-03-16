from rest_framework.permissions import BasePermission

class IsOwner(BasePermission) :

    def has_object_permission(self, request, view, obj):
        return True if request.user == obj.created_by else False