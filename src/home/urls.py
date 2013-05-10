# -*- coding: UTF-8 -*-
#URLS do módulo home

from django.conf.urls.defaults import patterns


urlpatterns = patterns('home.views',
                       (r'^$', 'home'),
                       (r'^gerdata/$', 'gerdata'),
                       (r'^impdata/$', 'impdata'),
#                       (r'^match/$', views.match),
                       )
