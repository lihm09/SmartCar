# encoding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts.utils import send_activation_email, new_activation_code
from accounts.models import ActivationCode

#登陆表单
class signin_form(AuthenticationForm):
    username = forms.RegexField(label="用户名",regex=r'^[a-z0-9-]{3,16}$',
        error_messages={'required':'啊，用户名被吃掉了！','invalid':'用户名不对哦！'})

    password = forms.RegexField(label="密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不对哦！'})

    error_messages = {
        'invalid_login': "咦？用户名或密码不对哦……",
        'no_cookies': "您的浏览器不支持cookies哦……",
        'inactive': "您的账号未激活，已重新发送激活邮件，请查收……",
        'send_mail_fail': "您的账号未激活，而且发送激活邮件失败，请联系管理员以解决问题……",
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
                activation_cache=ActivationCode.objects.get(user=self.user_cache).activation_code
                if send_activation_email(email=self.user_cache.email,username=self.user_cache.username,code=activation_cache):
                    raise forms.ValidationError(self.error_messages['inactive'])
                else:
                    raise forms.ValidationError(self.error_messages['send_mail_fail'])
        self.check_for_test_cookie()
        return self.cleaned_data


#注册表单
class signup_form(forms.Form):
    username = forms.RegexField(label="用户名",regex=r'^[a-z0-9-]{3,16}$',
        help_text='用户名只能由数字，小写字母，和短横组成，而且需在3-16位',
        error_messages={'required':'啊，用户名被吃掉了！','invalid':'用户名不对哦！'})

    email = forms.EmailField(label="邮箱",
        error_messages={'required':'啊，邮箱地址被吃掉了！','invalid':'这个真的是邮箱地址吗？'})

    password1 = forms.RegexField(label="密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        help_text='用户名只能由数字，大小写字母，短横和下划线组成，而且需在6-18位',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不符合要求哦！'})

    password2 = forms.RegexField(label="确认密码", widget=forms.PasswordInput,regex=r'^[a-z0-9-_]{6,18}$',
        help_text='再次输入密码以确认',
        error_messages={'required':'啊，密码被吃掉了！','invalid':'密码不符合要求哦！'})


    error_messages = {
        'duplicate_username': "已经有人抢先注册这个名字了哦……",
        'duplicate_email': "咦？这个邮箱地址已经被注册过了哦……",
        'password_mismatch': "咦？怎么跟上面的密码不一样呢？",
        'send_mail_fail': "注册成功,但是未能发送激活邮件，请联系管理员以解决问题……",
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError(self.error_messages['duplicate_email'])
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'])
        return password2

    def sav(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')

        new_user=User.objects.create_user(username,email,password)
        new_user.is_active=False
        new_user.save()

        activation_code=new_activation_code()
        activation_cache=ActivationCode.objects.create(user=new_user,activation_code=activation_code)

        if send_activation_email(email=email,username=username,code=activation_code):
            activation_cache.mail_sent_or_not=True
            activation_cache.save()
        else:
            raise forms.ValidationError(self.error_messages['send_mail_fail'])

        return new_user




#激活表单（填写详细资料）
class confirm_form(forms.Form):
    pass