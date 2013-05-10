from django.conf.urls.defaults import *

from imoveis import views


urlpatterns = patterns('',
                       url('^$', views.list),
                       url('^(?P<object_id>\d+)?/$', views.detail),
                       url('^add/$', views.add),
                       url('^delete/(?P<object_id>\d+)/(?P<assertion>./?)?$', views.delete),
                       url('^docs/(?P<object_id>\d+)/$', views.docs),
                       )