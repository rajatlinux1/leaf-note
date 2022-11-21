from django.shortcuts import render, redirect
from django.views import View
from .models import Users, Notes
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .utils import SendEmail, SendOTP
import uuid
from django.http import Http404
import random
from App.task import expire_otp
from django.core.exceptions import BadRequest
# Create your views here.


class Home(View):
    def get(self, request):
        # return render(request, 'App/two_factor.html',{'email':'uiuui'})
        # return render(request, 'email/otp_email.html',{'otp':12345, 'name':'Rajat'})
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, "App/pages-login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user=Users.objects.get(email=email)
            auth_user=authenticate(request, email=email, password=password)
            if auth_user is not None:
                #To verify email of user
                if auth_user.is_verify:
                    if user.twofactor:
                        if user.browser==request.META['HTTP_USER_AGENT'] and user.pass2f:
                            if remember:
                                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                            else:
                                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                            login(request, auth_user)
                        else:
                            user.otp=random.randrange(000000, 999999)
                            user.save()
                            SendOTP(email, user.otp)
                            id=user.id
                            expire_otp(id)
                            # asyncio.run_coroutine_threadsafe(expire_otp(pk=user.id), 1)
                            # async_to_sync(expire_otp(pk=user.id))
                            # sync_to_async(expire_otp(pk=user.id), thread_sensitive=True)
                            # asyncio.run(expire_otp(pk=user.id))
                            return render(request, 'App/two_factor.html',{'email':user.email})
                    else:
                        if remember:
                            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                        else:
                            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                        login(request, auth_user)
                else:
                    user.token=str(uuid.uuid4().hex)
                    user.save()
                    SendEmail(user.email, user.token, request.META['HTTP_HOST'])
                    messages.add_message(request, messages.ERROR, "Your email is'nt verify please check your mail box to get verified", extra_tags="info")
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, "Invalid Credentials", extra_tags="danger")
        except Users.DoesNotExist:
            messages.add_message(request, messages.ERROR, "You're not valid user please sign up", extra_tags="danger")
        except Exception as e:
            print(e)
        return redirect("home")



class Register(View):
    def get(self, request):
        return render(request, "App/pages-register.html")


    def post(self, request, *args, **kwrgs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('confirm_password')
        try:
            user=Users.objects.create(name=name, email=email)
            user.set_password(password)
            user.token=str(uuid.uuid4().hex)
            user.save()
            SendEmail(user.email, user.token, request.META['HTTP_HOST'])
            messages.add_message(request, messages.SUCCESS, "Check you're email box to verify email", extra_tags="success")
            return redirect('home')
        except:
            messages.add_message(request, messages.ERROR, "You're already registered please sign in", extra_tags="danger")
        print(name)
        print(email)
        print(password)
        return redirect("register")


@login_required
def index(request):
    if request.user.is_authenticated:
        note=Notes.objects.filter(user=request.user).order_by("-id")
        return render(request, 'App/index.html', {'note':note})


@login_required
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'App/users-profile.html')


@login_required
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')


def verify_email(request, token):
    if token:
        try:
            user=Users.objects.get(token=token)
            user.is_verify=True
            # user.token=None
            user.save()
            messages.add_message(request, messages.SUCCESS, "Your email successfully verified", extra_tags="success")
            return redirect('home')
        except:
            raise BadRequest



def resend(request, email):
    if email:
        try:
            user=Users.objects.get(email=email)
            user.otp=random.randrange(000000, 999999)
            user.save()
            SendOTP(email, user.otp)
            expire_otp(pk=user.id)
            messages.add_message(request, messages.SUCCESS, "OTP resend successfully", extra_tags="success")
            return render(request, 'App/two_factor.html',{'email':email})
        except:
            messages.add_message(request, messages.ERROR, "OTP resend failed", extra_tags="danger")
            return render(request, 'App/two_factor.html',{'email':email})


def verify_two_factor(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        try:
            global user
            user=Users.objects.get(otp=otp)
            user.pass2f=True
            user.browser=request.META['HTTP_USER_AGENT']
            user.otp=None
            user.save()
            return redirect('home')
        except Users.DoesNotExist:
            messages.add_message(request, messages.ERROR, "wrong Otp", extra_tags="danger")
            return render(request, 'App/two_factor.html',{'email':user.email})


class Note(View):
    def get(self, request, *args, **kwrgs):
        pass

    def post(self, request, *args, **kwrgs):
        pass

    def put(self, request, id, *args, **kwrgs):
        pass

    def delete(self, request, id, *args, **kwrgs):
        pass





def term_and_conditions(request):
    return render(request, 'App/terms_and_conditions.html')



#Error Functions

def NotFound_404(request, exception):
    return render(request, "errors/404.html")

def InternalServerError_500(request):
    return render(request, "errors/500.html")

def Forbidden_403(request, exception):
    return render(request, "errors/403.html")

def BadRequest_400(request, exception):
    return render(request, "errors/400.html")