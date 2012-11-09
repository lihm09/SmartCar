from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'SmartCar.views.index'),
    url(r'^about/$', 'SmartCar.views.about'),
    url(r'^manage/', include(admin.site.urls)),
    url(r'^accounts/',include('accounts.urls')),

    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':'./media/'}),

)
