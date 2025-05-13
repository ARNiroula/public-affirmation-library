from rest_framework import viewsets, mixins

# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.db.models import Prefetch

from .serializers import ExhibitionSerializer
from .models import Exhibition
from user.models import User
# Create your views here.


@extend_schema(tags=["event"])
class ExhibitionViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    serializer_class = ExhibitionSerializer
    queryset = Exhibition.objects.prefetch_related(  # pyright: ignore
        Prefetch(
            "users",
            queryset=User.objects.all(),
            to_attr="users_list",
        )
    )  # pyright: ignore

    def get_serializer_context(self):
        ctx = super().get_serializer_context() | {"request": self.request}
        return ctx
