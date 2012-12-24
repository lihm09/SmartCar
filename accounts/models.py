# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from accounts.settings import GENDER_CHOICES, DEPARTMENT_CHOICES

#用户激活码，激活后删除
class ActivationCode(models.Model):
    user = models.OneToOneField(User,unique=True,verbose_name='用户')
    activation_code = models.CharField('激活码',max_length=40)
    mail_sent_or_not = models.BooleanField('是否已发送验证邮件',default=False)

    class Meta:
        verbose_name='激活码'
        verbose_name_plural='激活码'

    def __str__(self):
        return self.user.username


#用户信息
class MyProfile(models.Model):
    user = models.OneToOneField(User,unique=True,verbose_name='用户')
    #team = models.ForeignField(verbose_name=('队伍'))
    real_name = models.CharField('姓名',max_length=10)
    mobile = models.CharField('手机', max_length=11)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='M')
    department = models.CharField('院系',max_length=1,choices=DEPARTMENT_CHOICES, default='a')
    class_name = models.CharField('班级',max_length=6)
    dormitory = models.CharField('宿舍',max_length=12)

    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = "用户资料"

    def __unicode__(self):
        return self.real_name

