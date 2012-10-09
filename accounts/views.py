# encoding: utf-8

import urlparse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from accounts.forms import signin_form
from SmartCar.settings import *



def index(request):
    pass


#登陆
def signin(request):
    redirect_to = request.REQUEST.get('next', '')

    if request.method == 'POST':
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

    elif request.user.is_authenticated():
        return redirect('/')
    else:
        form=signin_form(request)
        request.session.set_test_cookie()
        return render(request, 'accounts/signin.html',{'form':form})

#注销
def signout(request):
    auth.logout(request)
    return redirect('/')

#注册
def signup(request):
    if request.method is 'post':
        pass
    else:
        return render(request,'accounts/signup.html')
    pass




def confirm(request,code):
    pass



