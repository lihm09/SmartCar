from django.conf.urls import patterns,include, url

urlpatterns = patterns('team.views',
    url(r'^$','index',name='team_index'),
    #url(r'^(?P<num>[\w]+)/$','detail'),
)