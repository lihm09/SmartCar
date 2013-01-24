from django.conf.urls import patterns,include, url

urlpatterns = patterns('discuss.views',
    url(r'^$','index',name='discuss_index'),
    url(r'^(?P<num>[0-9]+)/$','detail'),
)