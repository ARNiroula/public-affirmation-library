from django.contrib.auth import get_user_model
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
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
    UserPwdForgotSerializer,
    UserStatusResponseSerializer,
    UserPwdResetSerializer,
)
from .permissions import (
    AdminPermissionMixin,
    CustomerPermissionMixin,
    IsNotAuthenticated,
)
from utils.redis import redis_client
from utils.otp import create_otp


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
    # permission_classes = [IsNotAuthenticated]
    authentication_classes = []
    permission_classes = []

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
class LogoutView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request):
        refresh_token = request.COOKIES.get("refresh_token")
        response = Response({"message": "Logged Out!"}, status=status.HTTP_200_OK)
        if refresh_token:
            try:
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
            except Exception as e:
                return Response(
                    {"error": f"Error invalidating token: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            response.delete_cookie(key="access_token")
            response.delete_cookie(key="refresh_token")
            if request.COOKIES.get("csrftoken"):
                response.delete_cookie(key="csrftoken")
            if request.COOKIES.get("sessionid"):
                response.delete_cookie(key="sessionid")

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

        # if request.data.get
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


@extend_schema(
    tags=["user"],
    responses={status.HTTP_200_OK: dict},
)
class ForgotPassword(APIView):
    """
    Route for User Forgot Password Sending
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserPwdForgotSerializer

    def post(self, request: Request):
        otp_code = create_otp()
        email = request.data.get("email")  # pyright: ignore

        if not get_user_model().objects.filter(email=email).exists():
            return Response(
                {"message": "Invalid Email sent"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        redis_client.setex(
            f"email:{email}",
            60 * 10,
            str(otp_code),
        )  # It will expire in 10 minutes

        send_mail(
            subject="PAL Library OTP Code",
            message=f"The OTP code is {otp_code}. It will expire in 10 minutes",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"message": "Email Sent!"}, status=status.HTTP_200_OK)


@extend_schema(
    tags=["user"],
    responses={status.HTTP_200_OK: dict},
)
class ResetPassword(APIView):
    """
    Route for User Forgot Password Sending
    """

    permission_classes = [AllowAny]
    authentication_classes = []
    serializer_class = UserPwdResetSerializer

    def patch(self, request: Request):
        check_otp_code = request.data.get("otp_code")  # pyright: ignore
        email = request.data.get("email")  # pyright: ignore

        try:
            user = get_user_model().objects.get(email=email)
        except Exception:
            return Response(
                {"message": "Invalid Email sent"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user.role != "customer":
            return Response(
                {"message": "Invalid Email sent"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        key = f"email:{email}"
        otp_code = redis_client.get(key)
        if otp_code != check_otp_code:
            return Response(
                {"message": "Invalid Code"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        new_pwd = request.data.get("new_pwd")  # pyright: ignore

        serializer = UserProfileSerializer(
            user,
            data={"password": new_pwd},
            partial=True,
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        redis_client.delete(key)
        return Response(data={"message": "Password Updated"}, status=status.HTTP_200_OK)
