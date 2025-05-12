import pyotp

from django.conf import settings

topt = pyotp.TOTP(settings.OTP_CRED)


def create_otp():
    return topt.now()
