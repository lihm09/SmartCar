# encoding: utf-8

from django.db import models
import time

class Discuss(models.Model):
    title = models.CharField('槽点', max_length=50)
    author = models.CharField('哪位槽神',max_length=50)
    content = models.TextField('内涵', max_length=1000)
    top = models.BooleanField('神吐槽', default=False)
    post_time = models.DateTimeField('吐槽时刻', auto_now_add=True)
    audience = models.PositiveIntegerField('围观群众', default=0)

    class Meta:
        verbose_name = "吐槽"
        verbose_name_plural = "吐槽"

    def __unicode__(self):
        return self.title
