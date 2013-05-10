# -*- coding: UTF-8 -*-

'''
Created on 10/05/2009

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.conf.urls import patterns, url
# Project Imports


urlpatterns = patterns('clientes.views',
                       url(r'^$', 'list'),
                       url(r'^(?P<object_id>\d+)/$', 'detail'),
                       url(r'^add/$', 'add'),
                       url(r'^delete/(?P<object_id>\d+)/(?P<assertion>./?)?$', 'delete'),
                       )
