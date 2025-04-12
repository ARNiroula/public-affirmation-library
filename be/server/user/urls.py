from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CreateCustomerView, StaffViewSet, UserProfileView


router = DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    # User Routes
    path("customer/register/", CreateCustomerView.as_view(), name="Register Customer"),
    path("profile", UserProfileView.as_view(), name="Show the Profile of the User"),
    path("", include(router.urls)),
]
