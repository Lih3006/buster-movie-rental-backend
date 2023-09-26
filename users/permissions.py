from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsEmployeePermission(permissions.BasePermission):
    def has_permission(self, request:Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )
      
        
class IsUserLoged(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return (request.user.is_authenticated and request.user == obj or request.user.is_superuser)