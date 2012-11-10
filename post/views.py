from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from post.models import Announcement
from post.settings import POST_PER_PAGE

def index(request):
    top=Announcement.objects.filter(top=True).order_by('post_time')
    rest=Announcement.objects.filter(top=False).order_by('post_time')

    return render(request, 'post/index.html',{'top':top,'rest':rest})