# -*- coding: UTF-8 -*-
#URLS do módulo financeiro

from django.conf.urls.defaults import *

from financeiro import views, models


urlpatterns = patterns('',
                       url('^$', views.home),
                       url(r'^Relatorio/', views.relatorio),
                       url(r'^(Pagamento)/', include('financeiro.innerurls'), {"model":models.Pagamento}),
                       url(r'^(Recebimento)/', include('financeiro.innerurls'), {"model":models.Recebimento}),
                       )