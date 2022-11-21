from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.
class Users(AbstractUser):
    username=None
    first_name=None
    last_name=None

    
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    profile_image=models.ImageField(upload_to='profile_images', null=True, blank=True)
    token=models.CharField(max_length=300)
    is_verify=models.BooleanField(default=False)


    twofactor=models.BooleanField(default=False)
    browser=models.CharField(max_length=200, null=True, blank=True)
    pass2f=models.BooleanField(default=False)
    otp=models.IntegerField(null=True, blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserManager()

    class Meta:
        db_table = "Users"

class Notes(models.Model):
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    time=models.TimeField(auto_now_add=True, null=True, blank=True)
    date=models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "Notes"
