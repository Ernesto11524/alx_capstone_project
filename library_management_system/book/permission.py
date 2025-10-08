from rest_framework import permissions

class IsStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
class StaffOnlyMixin:
    permission_classes = [permissions.IsAuthenticated, IsStaffPermission ]