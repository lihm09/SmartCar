# encoding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from utils import send_activation_email

#登陆表单
class signin_form(AuthenticationForm):
    username = forms.RegexField(label="用户名",regex=r'^[a-z0-9-]{3,16}$',
        error_messages={'required':'啊，用户名被吃掉了！','invalid':'用户名不对哦！'})

    password = forms.RegexField(label="密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不符合要求哦！'})

    error_messages = {
        'invalid_login': "咦？用户名或密码不对哦……",
        'no_cookies': "您的浏览器不支持cookies哦……",
        'inactive': "您的账号未激活，已重新发送激活邮件，请查收……",
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                if send_activation_email(request=self.request,user=self.user_cache):
                    raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data


#注册表单
class signup_form:
    username = forms.RegexField(label="用户名",regex=r'^[a-z0-9-]{3,16}$',
        help_text='用户名只能由数字，小写字母，和短横组成，而且需在3-16位',
        error_messages={'required':'啊，用户名被吃掉了！','invalid':'用户名不对哦！'})

    email = forms.EmailField(label="邮箱",
        error_messages={'required':'啊，邮箱地址被吃掉了！'})

    password1 = forms.RegexField(label="密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        help_text='用户名只能由数字，大小写字母，短横和下划线组成，而且需在6-18位',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不符合要求哦！'})

    password2 = forms.RegexField(label="确认密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        help_text='再次输入密码以确认',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不符合要求哦！'})


    error_messages = {
        'duplicate_username': "已经有人抢先起了这个名字了哦……",
        'password_mismatch': "咦？两个密码怎么不一样？",
        }