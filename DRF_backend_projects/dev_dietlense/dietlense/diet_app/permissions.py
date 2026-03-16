from rest_framework.permissions import BasePermission

from rest_framework import serializers

from diet_app.models import User

class IsOwner(BasePermission) :

    def has_object_permission(self, request, view, obj):

        if isinstance(obj,User) :

            return request.user == obj
        
        return request.user == obj.owner 
    
# class IsUser(BasePermission) :

#     def has_object_permission(self, request, view, obj):

#         return request.user.id == obj.id

class ProfileRequired(BasePermission):

    message = "user has no profile"

    def has_permission(self, request, view):

       try :
           
           profile = request.user.profile

           return True
       
       except :
           
           return False
       
class HasFoodLog(BasePermission) :

    message = "user has no foodlogs"

    def has_permission(self, request, view):
        
        try :
           
           foodlog = request.user.foodentries

           return True
       
        except :
           
           return False
           