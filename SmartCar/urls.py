from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'SmartCar.views.index'),
    url(r'^about/$', 'SmartCar.views.about'),
#    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':'./static/'}),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
