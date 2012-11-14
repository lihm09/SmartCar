from django.shortcuts import render,redirect
from post.models import Post, File
from django.db.models import ObjectDoesNotExist
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from post.settings import POST_PER_PAGE
from SmartCar.settings import MEDIA_URL

def index(request):
    top=Post.objects.filter(top=True).order_by('-post_time')
    rest=Post.objects.filter(top=False).order_by('-post_time')
    return render(request, 'post/index.html',{'top':top,'rest':rest})

def detail(request,num):
    try:
        this_post=Post.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404
    this_post.hits+=1
    this_post.save()
    if this_post.file:
        return redirect(MEDIA_URL+this_post.file.file.name)
    return render(request, 'post/detail.html',{'this_post':this_post})
