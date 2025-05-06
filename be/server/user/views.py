from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from drf_spectacular.utils import extend_schema

from .serializers import (
    CustomerRegisterSerializer,
    StaffRegisterSerializer,
    UserProfileSerializer,
    UserLoginSerializer,
    UserLoginResponseSerializer,
    UserLogoutResponseSerializer,
    UserStatusResponseSerializer,
)
from .permissions import (
    AdminPermissionMixin,
    CustomerPermissionMixin,
    IsNotAuthenticated,
)


# Create your views here.
@extend_schema(tags=["user"])
class CreateCustomerView(CreateAPIView):
    model = get_user_model()
    permission_classes = [IsNotAuthenticated]
    serializer_class = CustomerRegisterSerializer


@extend_schema(tags=["user"])
class StaffViewSet(AdminPermissionMixin, viewsets.ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = StaffRegisterSerializer


@extend_schema(tags=["user"])
class LoginView(APIView):
    permission_classes = [IsNotAuthenticated]

    @extend_schema(
        request=UserLoginSerializer,
        responses={200: UserLoginResponseSerializer},
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return response

        user = serializer.validated_data
        refresh_token = RefreshToken.for_user(user)  # pyright: ignore
        access_token = str(refresh_token.access_token)
        response = Response(
            {
                "user": UserProfileSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="None",
        )
        response.set_cookie(
            key="refresh_token",
            value=str(refresh_token),
            httponly=True,
            secure=True,
            samesite="None",
        )

        return response


@extend_schema(
    tags=["user"],
    request=None,
    responses={status.HTTP_200_OK: UserLogoutResponseSerializer},
)
class LogoutView(CustomerPermissionMixin, APIView):
    def post(self, request: Request):
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
            except Exception as e:
                return Response(
                    {"error": f"Error invalidating token: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        response = Response({"message": "Logged Out!"}, status=status.HTTP_200_OK)
        response.delete_cookie(key="access_token")
        response.delete_cookie(key="refresh_token")
        return response


@extend_schema(tags=["user"])
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"error": "Refresh Token Not Provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            response = Response(
                {"message": "Access Token Refreshed Successfully"},
                status=status.HTTP_200_OK,
            )
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="None",
            )
            response.set_cookie(
                key="refresh_token",
                value=str(refresh_token),
                httponly=True,
                secure=True,
                samesite="None",
            )

            return response
        except InvalidToken:
            return Response(
                {"error": "Invalid Refresh Token"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {"error": f"Token Creation Unsuccessful {str(e)}"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


@extend_schema(tags=["user"])
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


@extend_schema(
    tags=["user"], responses={status.HTTP_200_OK: UserStatusResponseSerializer}
)
class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"authenticated": True})
