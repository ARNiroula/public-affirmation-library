from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet, BookingViewSet

router = DefaultRouter()
router.register(r"room", RoomViewSet, basename="room")
router.register(r"booking", BookingViewSet, basename="booking")

urlpatterns = [path("", include(router.urls))]
