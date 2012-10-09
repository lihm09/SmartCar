# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from accounts.settings import GENDER_CHOICES, DEPARTMENT_CHOICES

#用户激活码，激活后删除
class ActivationCode(models.Model):
    user = models.OneToOneField(User,unique=True,verbose_name='用户')
    activation_key = models.CharField('激活码',max_length=40)

    class Meta:
        verbose_name='激活码'
        verbose_name_plural='激活码'

    def __str__(self):
        return self.user.username


#用户信息
class MyProfile(models.Model):
    user = models.OneToOneField(User,unique=True,verbose_name='用户')
    #team = models.ForeignField(verbose_name=('队伍'))
    mobile = models.CharField('手机',unique=True, max_length=11)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='M')
    department = models.CharField('院系',max_length=2,choices=DEPARTMENT_CHOICES)
    class_name = models.CharField('班级',max_length=5)
    dormitory = models.CharField('宿舍',max_length=10)

    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = "用户资料"

    def __str__(self):
        if self.user.last_name and self.user.first_name:
            return self.user.last_name+self.user.first_name
        else:
            return self.user.username

