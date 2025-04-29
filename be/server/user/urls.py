from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CreateCustomerView,
    StaffViewSet,
    UserProfileView,
    LogoutView,
    LoginView,
    CookieTokenRefreshView,
)


router = DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    # User Routes
    path("customer/register/", CreateCustomerView.as_view(), name="Register Customer"),
    path("profile", UserProfileView.as_view(), name="Show the Profile of the User"),
    path("login/", LoginView.as_view(), name="User Login View"),
    path("logout/", LogoutView.as_view(), name="User Logout View"),
    path(
        "refresh/", CookieTokenRefreshView.as_view(), name="Refresh Token from Cookie"
    ),
    path("", include(router.urls)),
]
