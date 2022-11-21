from celery import shared_task
import time
from .models import Users
import asyncio
from asgiref.sync import async_to_sync
from Project.celery import app

@shared_task(bind=True)
def expire_otp(id):
    user=Users.objects.get(id=id)
    time.sleep(60)
    user.otp=None
    user.save()
    return f"{user.name}'s OTP has been removed"