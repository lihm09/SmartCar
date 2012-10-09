from django.conf.urls import patterns,include, url

urlpatterns = patterns('accounts.views',
    url(r'^$','index',name='accounts_index'),
    # Signup, signin and signout
    url(r'^signup/$','signup',name='signup'),
    url(r'^signin/$','signin',name='signin'),
    url(r'^signout/$','signout',name='signout'),
)