from django.conf.urls import patterns,include, url

urlpatterns = patterns('post.views',
    url(r'^$','index',name='post_index'),

)