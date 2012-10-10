# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from team.settings import GENDER_CHOICES, DEPARTMENT_CHOICES


#队伍模型
class Team(models.Model):

    class Meta:
        verbose_name = "队伍"
        verbose_name_plural = "队伍"

    def __str__(self):
        pass


class UserInTeam(models.Model):
    pass