# encoding: utf-8

from django.core.mail import EmailMessage
from smtplib import SMTPException
from SmartCar.settings import SITE_NAME,ORG,EMAIL_HOST_USER
from django.template import loader, Context

import random, string

def send_activation_email(email,username,code):
    subject='['+SITE_NAME+']'+'Email地址验证'
    msg_context=Context({
        'site_name':SITE_NAME,
        'org':ORG,
        'username':username,
        'confirm_code':code
    })
    html_content=loader.get_template('accounts/confirm_message.html').render(msg_context)
    activation_msg=EmailMessage(subject,html_content,EMAIL_HOST_USER,[email])
    activation_msg.content_subtype="html"

    try:
        activation_msg.send(fail_silently=False)
    except:
        return False
    return True


def new_activation_code(random_length=40):
    return ''.join([(string.ascii_letters+string.digits)[x] for x in random.sample(range(0,62),random_length)])