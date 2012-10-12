# encoding: utf-8

import urlparse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from accounts.forms import signin_form, signup_form, confirm_form
from django import forms
from SmartCar.settings import LOGIN_REDIRECT_URL,SIGNUP_ACCESS

from accounts.models import ActivationCode


@login_required()
def index(request):
    render(request,'accounts/index.html')


#登陆
def signin(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.user.is_authenticated():
        return redirect('/accounts/')
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
        return render(request, 'accounts/signin.html',{'form':form,'next':redirect_to})

#注销
def signout(request):
    auth.logout(request)
    return redirect('/')

#注册
def signup(request):
    if request.user.is_authenticated():
        return redirect('/accounts/')
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


def confirm(request,code=None):
    if request.user.is_authenticated():
        return redirect('/accounts/')
    else:
        try:
            activation_cache=ActivationCode.objects.get(activation_code=code)
        except ActivationCode.DoesNotExist:
            return render(request,'accounts/confirm_invalid.html')

        if request.method == 'POST':
            form=confirm_form(data=request.POST)
            if form.is_valid():
                form.sav(user=activation_cache.user)
                activation_cache.user.is_active=True
                activation_cache.user.save()
                activation_cache.delete()
                return render(request,'accounts/confirm_succeed.html')
            else:
                return render(request,'accounts/confirm.html',{'form':form})
        else:
            form = confirm_form
            return render(request,'accounts/confirm.html',{'form':form})



