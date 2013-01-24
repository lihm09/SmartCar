from django.shortcuts import render,redirect
from discuss.models import Discuss
from django.db.models import ObjectDoesNotExist, Q
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from discuss.settings import POST_PER_PAGE
from SmartCar.settings import MEDIA_URL

def index(request):
    s=request.GET.get('s')
    if s:
        rest=Discuss.objects.filter(Q(content__contains=s) | Q(title__contains=s)).order_by('-post_time')
        return render(request, 'discuss/search.html',{'s':s,'rest':rest})
    top=Discuss.objects.filter(top=True).order_by('-post_time')
    rest=Discuss.objects.filter(top=False).order_by('-post_time')
    return render(request, 'discuss/index.html',{'top':top,'rest':rest})

def detail(request,num):
    try:
        this_discuss=Discuss.objects.get(id=num)
    except ObjectDoesNotExist:
        raise Http404
    this_discuss.audience+=1
    this_discuss.save()
    return render(request, 'discuss/detail.html',{'this_discuss':this_discuss})
