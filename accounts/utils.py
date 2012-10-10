# encoding: utf-8

from django.shortcuts import render
from django.core.mail import send_mail
from smtplib import SMTPException
from SmartCar.settings import *
from django.template import loader, Context

import random, string

def send_activation_email(request,user):

    activation_msg=loader.get_template('accounts/confirm_message.html')
    msg_context=Context({})

    try:
        send_mail('['+SITE_NAME+']'+'Email地址验证', activation_msg.render(msg_context), EMAIL_HOST_USER,[user_email], fail_silently=False)
    except SMTPException:
        return render(request,'accounts/sendmail_fail.html')

    return True



def new_activation_code(random_length=40):
    return ''.join([(string.ascii_letters+string.digits)[x] for x in random.sample(range(0,62),random_length)])