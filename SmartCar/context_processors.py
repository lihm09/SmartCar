# encoding: utf-8
import datetime

def siteinfo(request):
    info={'site_name':'第八届智能车竞赛',
          'year':datetime.datetime.now().year,
          'org':'清华大学工程物理系学生科协'}
    return info