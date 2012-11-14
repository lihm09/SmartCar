# encoding: utf-8

from django.db import models
import os
from django.db.models.signals import post_delete
import time

class File(models.Model):
    file = models.FileField('文件', upload_to=time.strftime("%b-%d", time.localtime())+'/')
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)
    hits = models.PositiveIntegerField('下载量', default=0)

    class Meta:
        verbose_name = "文件"
        verbose_name_plural = "文件"

    def __unicode__(self):
        return self.file.name


class Post(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容', max_length=1000)
    top = models.BooleanField('置顶', default=False)
    file = models.OneToOneField(File,verbose_name='附件',blank=True)
    post_time = models.DateTimeField('发布时间', auto_now_add=True)
    hits = models.PositiveIntegerField('点击量', default=0)

    class Meta:
        verbose_name = "公告"
        verbose_name_plural = "公告"

    def __unicode__(self):
        return self.title

#删除数据之后也删除文件
def delete_file(sender, **kwargs):
    patch = kwargs['instance']
    os.remove(patch.file.path)
post_delete.connect(delete_file, sender=File)
