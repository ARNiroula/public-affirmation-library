from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permission for Admins Only
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.role == "admin")


class IsStaff(BasePermission):
    """
    Permission for Admin and Staff
    """

    def has_permission(self, request, view):  # pyright: ignore
        if request.user.is_authenticated:
            return request.user.role in {"admin", "staff"} or request.user.is_staff
        return False


class IsCustomer(BasePermission):
    """
    Permission for Customer
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsNotAuthenticated(BasePermission):
    """
    Check if there is authentication in the header or not
    """

    def has_permission(self, request, view):  # pyright: ignore
        return not request.user.is_authenticated


class IsOwnerOrStaff(BasePermission):
    """
    Check if the resource is associated with the owner or the staff
    e.g. Booking, Rental, etc.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class CustomerPermissionMixin:
    permission_classes = [IsCustomer]


class StaffPermissionMixin:
    permission_classes = [IsStaff]


class AdminPermissionMixin:
    permission_classes = [IsAdmin]
