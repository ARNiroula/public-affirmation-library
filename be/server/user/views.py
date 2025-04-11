from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model

from .serializers import CustomerRegisterSerializer, StaffRegisterSerializer
from .permissions import AdminPermissionMixin, CustomerPermissionMixin


# Create your views here.
class CreateCustomerView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerRegisterSerializer


class StaffViewSet(AdminPermissionMixin, viewsets.ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = StaffRegisterSerializer


# class CreateStaffView(AdminPermissionMixin, CreateAPIView):
#     model = get_user_model()
#     queryset = model.objects.all()
#     serializer_class = StaffRegisterSerializer


class CustomerProfileView(CustomerPermissionMixin, RetrieveAPIView):
    model = get_user_model()

    def get(self, request):
        return Response(
            {
                "username": request.user.username,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "role": request.user.role,
                "date_joined": request.user.date_joined,
            }
        )
