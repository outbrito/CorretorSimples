# -*- coding: UTF-8 -*-

'''
Created on 30/05/2009

@author: ThiagoP
'''

# Python Imports
# Django Imports
from django.conf.urls import patterns, url, include
# Project Imports
from clientes import models


urlpatterns = patterns('clientes.views',
                       url(r'^$', 'home'),
                       url(r'^(Proprietario)/', include('clientes.innerurls'), {'model': models.Proprietario}),
                       url(r'^(Comprador)/', include('clientes.innerurls'), {'model': models.Comprador}),  
                       )