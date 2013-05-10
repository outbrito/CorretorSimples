# -*- coding: UTF-8 -*-

from shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from financeiro import models
from financeiro.querymanager import *
from financeiro import myforms

import reports


MODULE = "> Financeiro "

REPORTS = ((1,"Vendas Por Categoria"), (2,"Financeiro"), (3,"Cadastro de Imóveis"))


@login_required
def home(request):
    cs_list = [models.__getattribute__(cs) for cs in models.__all__]
    for cs in cs_list:
        cs.opts = cs._meta
    
    response = render_to_response("financeiro/home.html",
                                  {
                                   "module":MODULE,
                                   "cs_list":cs_list,
                                   },
                                  request
                                  )
    return response


@login_required
def list(request, model):
    if request.GET.get('busca',''):
        param = request.GET.get('busca','')
        mov_list = model.objects.filter(make_query(param))
    else:
        mov_list = model.objects.all()

    response = render_to_response("financeiro/list.html",
                                  {
                                   "module":MODULE,
                                   "mov_list":mov_list,
                                   },
                                  request
                                  )
    return response


@login_required
def detail(request, model, object_id):
    object = model.objects.get(pk=object_id)
    ObjectFormFactory = modelform_factory(model, form=myforms.CostumizedModelForm)
    
    if request.method == 'POST':
        form = ObjectFormFactory(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('financeiro.views.list', args=(model.__name__,)))
        
    else:
        form = ObjectFormFactory(instance=object)
    
    response = render_to_response("financeiro/detail.html",
                                 { 
                                  "module":MODULE+"> Adicionar ",
                                  "form": form,
                                  },
                                  request
                                 )
    return response
    

@login_required
def add(request, model):
    ObjectFormFactory = modelform_factory(model, form=myforms.CostumizedModelForm)
    
    if request.method == 'POST':
        form = ObjectFormFactory(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('financeiro.views.list', args=(model.__name__,)))
    else:
        form = ObjectFormFactory()
    
    response = render_to_response("financeiro/add.html",
                                 { 
                                  "module":MODULE+"> Adicionar ",
                                  "form": form,
                                  },
                                  request
                                 )
    return response


@login_required   
def delete(request, model, object_id, assertion="n"):
    object = model.objects.get(pk=object_id)
    
    if str(assertion).lower() == "s":   
        object.delete()
        return HttpResponseRedirect(reverse('financeiro.views.list', args=(model.__name__,)))
    else:
        response = render_to_response("financeiro/delete.html",
                                      {
                                       "module":MODULE+"> Deletar ",
                                       "movimento":object,
                                       },
                                      request
                                      )
    return response


@login_required
def relatorio(request):
    chart_path = ""
    
    if request.method == 'POST':
        opt = request.POST.get('relatorio','')
        ano = request.POST.get('ano','')
        
        if opt == "1":
            chart_path = reports.VendasPorCategoria(ano)
        elif opt == "2":
            chart_path = reports.Financeiro(ano)
        elif opt == "3":
            chart_path = reports.CadastroImoveis(ano)
        elif opt == "4":    
            chart_path = reports.EvolucaoVendasPorCategoria(ano)
        elif opt == "5":    
            chart_path = reports.EvolucaoFinanceira(ano)
        elif opt == "6":    
            chart_path = reports.EvolucaoCadastroImoveis(ano)
    
    form_reportq = myforms.FormReport()
    
    response = render_to_response("financeiro/reports.html",
                                 { 
                                  "module":MODULE+"> Relatórios ",
                                  "form_reportq": form_reportq,
                                  "chart_path":chart_path,
                                  },
                                  request
                                 )
    return response