from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView, Response

from .serializers import (
    CustomerRegisterSerializer,
    StaffRegisterSerializer,
    UserProfileSerializer,
)
from .permissions import (
    AdminPermissionMixin,
    CustomerPermissionMixin,
    IsNotAuthenticated,
)


# Create your views here.
class CreateCustomerView(CreateAPIView):
    model = get_user_model()
    permission_classes = [IsNotAuthenticated]
    serializer_class = CustomerRegisterSerializer


class StaffViewSet(AdminPermissionMixin, viewsets.ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = StaffRegisterSerializer


class UserProfileView(
    CustomerPermissionMixin,
    APIView,
):
    model = get_user_model()
    serializer_class = UserProfileSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_object(self):
        try:
            return self.model.objects.get(pk=self.request.user.id)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request):
        if len(request.data) == 0:
            return Response("No Update Data", status=status.HTTP_304_NOT_MODIFIED)

        user = self.get_object()

        serializer = self.serializer_class(user, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
