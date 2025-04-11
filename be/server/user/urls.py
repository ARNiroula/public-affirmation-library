from django.urls import path

from .views import CreateCustomerView, CreateStaffView, CustomerProfileView

urlpatterns = [
    # User Routes
    path("customer/register/", CreateCustomerView.as_view(), name="Register Customer"),
    path("staff/register/", CreateStaffView.as_view(), name="Register Customer"),
    path("customer/profile", CustomerProfileView.as_view(), name="Register Customer"),
]
