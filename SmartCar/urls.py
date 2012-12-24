from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'SmartCar.views.index',name='home'),
    url(r'^about/$', 'SmartCar.views.about',name='about'),
    url(r'^manage/', include(admin.site.urls)),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^post/', include('post.urls')),
)
