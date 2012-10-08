# encoding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
        unique=True,
        verbose_name=_('user'),
        related_name='my_profile')
    favourite_snack = models.CharField('最喜欢吃',
        max_length=5)

    class Meta:
        verbose_name="用户资料"
        verbose_name_plural="用户资料"

    def __str__(self):
        return self.user.username
