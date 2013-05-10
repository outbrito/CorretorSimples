# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'contas/login.html'}),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       
    url(r'^clientes/', include('clientes.urls')),
    url(r'^financeiro/', include('financeiro.urls')),
    url(r'^imoveis/', include('imoveis.urls')),
    url(r'^contato/', include('contato.urls')),
    url(r'^conta/', include('contas.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    
    (r'^', include('home.urls')),

#    import django.views.static.serve
#    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../templates', 'show_indexes': True}),
#	(r'^CORRETOR/export/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '../CORRETOR/export', 'show_indexes': True}),
)
