# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from team.settings import TYPE_CHOICES, STATUS_CHOICES


#队伍模型
class Team(models.Model):
    slug = models.SlugField('队伍代号', unique=True, max_length=10)
    name = models.CharField('队伍名称', unique=True, max_length=20)
    leader = models.OneToOneField(User, unique=True, verbose_name='队长')
    type = models.CharField('参赛组别', max_length=1, choices=TYPE_CHOICES, default='a')
    car_taken = models.BooleanField('已经取车',default=False)
    status = models.CharField('队伍状态', max_length=1, choices=STATUS_CHOICES, default='a')

    class Meta:
        verbose_name = "队伍"
        verbose_name_plural = "队伍"

    def __str__(self):
        return self.name


class UserInTeam(models.Model):
    team = models.ForeignKey(Team, verbose_name='队伍')
    user = models.OneToOneField(User, unique=True, verbose_name='队员')