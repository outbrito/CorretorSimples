# -*- coding: UTF-8 -*-

from shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.models import modelform_factory
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from clientes import models
from clientes import querymanager

from imoveis import models as imoveis_models
from extras.model_match import make_match

TIPO = ((0, 'Casa'), (1, 'Apartamento'), (2, 'Flat'), (3, 'Terreno'), (4, 'Granja'), (5, 'Chacara'), (6, 'Fazenda'), (7, 'Hotel'), (8, 'Pousada'), (9, 'Loja'), (10, 'Sala'), (11, 'Galpao'), (12, 'Cobertura'), (13, 'Duplex'), (14, 'Outros') )


@login_required
def home(request):
    cs_list = [models.__getattribute__(cs) for cs in models.__all__]
    for cs in cs_list:
        cs.opts = cs._meta
        
    response = render_to_response("clientes/home.html",
                                  {
                                   "path": [
                                            ('Clientes', reverse('clientes.views.home')),
                                           ],
                                   "cs_list": cs_list,
                                   },
                                  request
                                  )
    return response


@login_required
def list(request, model):
    if request.GET.get('busca',''):
        param = request.GET.get('busca','')
        cliente_lista = model.objects.filter(make_query(param))
    else:
        cliente_lista = model.objects.all()

    response = render_to_response("clientes/list.html",
                                  {
                                   "path": [
                                            ('Clientes', reverse('clientes.views.home')),
                                            (model.__name__, reverse('clientes.views.list', args=(model.__name__,))),
                                           ],
                                   "cliente_lista":cliente_lista,
                                   },
                                  request
                                  )
    return response


@login_required
def detail(request, model, object_id):
    object = model.objects.get(pk=object_id)
    ObjectFormFactory = modelform_factory(model)
    
    if request.method == 'POST':
        form = ObjectFormFactory(request.POST, instance=object)
        if form.is_valid():
            inst = form.save()
            
            if inst.__class__.__name__ == "Comprador":
                return match(inst)
            else:
                return HttpResponseRedirect(reverse('clientes.views.list', args=(model.__name__,)))
    else:
        form = ObjectFormFactory(instance=object)
    
    response = render_to_response("clientes/detail.html",
                                 { 
                                  "path": [
                                            ('Clientes', reverse('clientes.views.home')),
                                            (model.__name__, reverse('clientes.views.list', args=(model.__name__,))),
                                            ("Detalhes", reverse('clientes.views.detail', args=(model.__name__, object_id))),
                                        ],
                                  "form": form,
                                  },
                                  request
                                 )
    return response
    

@login_required
def add(request, model):
    ObjectFormFactory = modelform_factory(model)
    
    if request.method == 'POST':
        form = ObjectFormFactory(request.POST)
        if form.is_valid():
            inst = form.save()
            
            if inst.__class__.__name__ == "Comprador":
                return match(inst)
            else:
                return HttpResponseRedirect(reverse('clientes.views.list', args=(model.__name__,)))
    else:
        form = ObjectFormFactory()
    
    response = render_to_response("clientes/add.html",
                                 { 
                                  "path": [
                                            ('Clientes', reverse('clientes.views.home')),
                                            (model.__name__, reverse('clientes.views.list', args=(model.__name__,))),
                                            ("Adicionar", reverse('clientes.views.add', args=(model.__name__,))),
                                          ],
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
        return HttpResponseRedirect(reverse('clientes.views.list', args=(model.__name__,)))
    else:
        response = render_to_response("clientes/delete.html",
                                      {
                                       "path": [
                                                ('Clientes', reverse('clientes.views.home')),
                                                (model.__name__, reverse('clientes.views.list', args=(model.__name__,))),
                                                ("Deletar", reverse('clientes.views.delete', args=(model.__name__, object_id))),
                                               ],
                                       "cliente":object,
                                       },
                                      request
                                      )
    return response



def match(inst):
    
    model = imoveis_models.__getattribute__(models.TIPO[inst.tipo][1])
    
    
    query = make_match(inst, model)
    
    match_list = model.objects.filter(query)
#    arq = open('f:/away.txt','w')
#    arq.write(str(match_list.query))
#    arq.close()
    
    response = render_to_response("match.html",
                                  {
                                   "module": "MATCH",
                                   "match_list":match_list,
                                   }
                                  )
    return response
