# encoding: utf-8

from django.db import models

class Announcement(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容', max_length=1000)
    top = models.BooleanField('置顶', default=False)
    post_time = models.DateTimeField('发布时间', auto_now=True)
    hits = models.PositiveIntegerField('点击量', default=0)
    #today_hits = models.PositiveIntegerField('今日点击量', default=0)

    class Meta:
        verbose_name = "公告"
        verbose_name_plural = "公告"

    def __unicode__(self):
        return self.title

class Download(models.Model):
    pass