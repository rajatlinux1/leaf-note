from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register', Register.as_view(), name='register'),
    path('index', index, name='index'),
    path('user_profile', user_profile, name='user_profile'),
    path('logout_user', logout_user, name='logout_user'),
    path('verify_email/<str:token>/', verify_email, name='verify_email'),
    path('resend/<str:email>/', resend, name='resend'),
    path('verify_two_factor', verify_two_factor, name='verify_two_factor'),
    path('term_and_conditions', term_and_conditions, name='term_and_conditions'),
    ]