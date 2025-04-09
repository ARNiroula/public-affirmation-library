from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permission for Admins Only
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class IsStaff(BasePermission):
    """
    Permission for Admin and Staff
    """

    def has_permission(self, request, view):  # pyright: ignore
        if request.user.is_authenticated:
            return request.user.role in {"admin", "staff"}
        return False


class IsCustomer(BasePermission):
    """
    Permission for Customer
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "customer"
