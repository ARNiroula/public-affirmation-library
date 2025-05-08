from django.urls import path

from .views import RentalView


urlpatterns = [
    path("rent/", RentalView.as_view(), name="Create Rents"),
]
