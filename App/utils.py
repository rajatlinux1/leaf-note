#This file contains all the third party functions which will call in view file.
#This file will contain all kind of third party functions.

import time
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import asyncio
from .models import Users

def SendEmail(email, token, host_name):
    subject="Email verification from NotePad"
    html_message=render_to_string('email/email_verify.html', {'token': token, 'host_name':host_name})
    plain_message=strip_tags(html_message)
    from_email=settings.EMAIL_HOST_USER
    to=email
    try:
        send_mail(
        subject, plain_message, from_email, [to], html_message=html_message
        )
        print(f"Email send successfully for {email}")
    except:
        print("Error occured in email")


def SendOTP(email, otp):
    subject="Two Factor Authentication from LeafNote"
    html_message=render_to_string('email/otp_email2.html',{'otp':otp})
    plain_message=strip_tags(html_message)
    from_email=settings.EMAIL_HOST_USER
    to=email
    try:
        send_mail(
        subject, plain_message, from_email, [to], html_message=html_message
        )
        print(f"Email send successfully for {email}")
    except:
        print("Error occured in email")


# async def expire_otp(pk):
#     print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
#     user=Users.objects.get(id=pk)
#     await asyncio.sleep(60)
#     user.otp=None
#     user.save()
#     print(f"{user.name}'s OTP has been removed")
    # return f"{user.name}'s OTP has been removed"


def expire_otp(pk):
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    user=Users.objects.get(id=pk)
    time.sleep(60)
    user.otp=None
    user.save()
    print(f"{user.name}'s OTP has been removed")