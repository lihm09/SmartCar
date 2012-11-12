from django.shortcuts import render
from post.models import Announcement
from django.db.models import ObjectDoesNotExist
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from post.settings import POST_PER_PAGE

def index(request):
    top=Announcement.objects.filter(top=True).order_by('-post_time')
    rest=Announcement.objects.filter(top=False).order_by('-post_time')

    return render(request, 'post/index.html',{'top':top,'rest':rest})

def detail(request,num):
    try:
        this_post=Announcement.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404
    this_post.hits+=1
    this_post.save()
    return render(request, 'post/detail.html',{'this_post':this_post})