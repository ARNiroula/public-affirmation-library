from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ExhibitionViewSet

router = DefaultRouter()
router.register(r"event", ExhibitionViewSet, basename="event")

urlpatterns = [path("", include(router.urls))]
