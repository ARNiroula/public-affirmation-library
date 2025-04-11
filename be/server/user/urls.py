from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CreateCustomerView, StaffViewSet, CustomerProfileView


router = DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    # User Routes
    path("customer/register/", CreateCustomerView.as_view(), name="Register Customer"),
    # path("staff/register/", CreateStaffView.as_view(), name="Register Customer"),
    path("customer/profile", CustomerProfileView.as_view(), name="Register Customer"),
    path("", include(router.urls)),
]
