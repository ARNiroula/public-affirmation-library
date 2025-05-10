from django.urls import path

from .views import RentalView, RentalCache


urlpatterns = [
    path("rent/", RentalView.as_view(), name="Create Rents"),
    path(
        "rent/cache",
        RentalCache.as_view(),
        name="Save Cart to Cache",
    ),
]
