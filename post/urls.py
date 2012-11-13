from django.conf.urls import patterns,include, url

urlpatterns = patterns('post.views',
    url(r'^$','index',name='post_index'),
    url(r'^(?P<num>[0-9]+)/$','detail',name='post_detail'),
    url(r'^file/(?P<num>[0-9]+)/$','file',name='post_file')
)