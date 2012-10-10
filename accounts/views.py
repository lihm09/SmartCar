# encoding: utf-8

import urlparse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from accounts.forms import signin_form, signup_form
from django import forms
from SmartCar.settings import *


def index(request):
    pass


#登陆
def signin(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.user.is_authenticated():
        return redirect('/')
    elif request.method == 'POST':
        form=signin_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]
            if not redirect_to:
                redirect_to = LOGIN_REDIRECT_URL
            elif netloc and netloc != request.get_host():
                redirect_to = LOGIN_REDIRECT_URL

            auth.login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return redirect(redirect_to)
        else:
            return render(request, 'accounts/signin.html',{'form':form})
    else:
        form=signin_form()
        request.session.set_test_cookie()
        return render(request, 'accounts/signin.html',{'form':form})

#注销
def signout(request):
    auth.logout(request)
    return redirect('/')

#注册
def signup(request):
    if request.user.is_authenticated():
        return redirect('/')
    elif not SIGNUP_ACCESS:
        return render(request,'accounts/signup_end.html')
    elif request.method == 'POST':
        form=signup_form(data=request.POST)
        if form.is_valid():
            try:
                form.sav()
            except forms.ValidationError:
                return render(request, 'accounts/signup.html',{'form':form})
            return render(request, 'accounts/sendmail_succeed.html',{'form':form})
        else:
            return render(request, 'accounts/signup.html',{'form':form})
    else:
        form=signup_form()
        return render(request,'accounts/signup.html',{'form':form})


def confirm(request,code):
    pass



