# -*- coding: UTF-8 -*-

import os
import shutil
import re

from shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.models import modelform_factory, inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from imoveis.models import Imovel, Attr
from imoveis.querymanager import make_query
from forms import ImovelForm
from settings import STATICFILES_DIRS 

from clientes import models as clientes_models
from extras.model_match import make_match


MODULE = "> Imóveis "

#def home(request):
#    cs_list = [models.__getattribute__(cs) for cs in models.__all__]
#    for cs in cs_list:
#        cs.opts = cs._meta
##    cs_list = models.__all__
#    response = render_to_response("imoveis/home.html",
#                                  {
#                                   "module":MODULE,
#                                   "cs_list": cs_list,
#                                   }
#                                  )
#    return response


@login_required
def list(request):
    
    if request.GET.get('negociacao',''):
        tipo = request.GET.get('negociacao','')
        mod_lista = Imovel.objects.filter(negocio=tipo)
        
        if request.GET.get('busca',''):
            param = request.GET.get('busca','')
            mod_lista = mod_lista.filter(make_query(param))
    else:
        mod_lista = Imovel.objects.all()
    
    response = render_to_response("imoveis/list.html",
                                  {
                                   "module":MODULE+"> Lista ",
                                   "mod_lista": mod_lista,
                                   },
                                  request
                                  )
    return response


@login_required
def detail(request, object_id):
    object = Imovel.objects.get(pk=object_id)
    
    ObjectFormFactory = inlineformset_factory(Imovel, Attr)
    
    if request.method == 'POST':
        form = ObjectFormFactory(request.POST, instance=object)
        
        form = ImovelForm(request.POST, instance=object)
        formset = ObjectFormFactory(request.POST, instance=object)
        
        if form.is_valid() and formset.is_valid():
            inst = form.save()
            attrs = formset.save()
            
            return match(inst)
            
    else:
        form = ImovelForm(instance=object)
        formset = ObjectFormFactory(instance=object)
    
    
    response = render_to_response("imoveis/detail.html",
                                 {
                                  "module":MODULE+"> Detalhes ",
                                  "form": form,
                                  "formset": formset,
                                  "object_id": object_id,
                                  },
                                  request
                             )
    return response
    

@login_required
def add(request):
    ObjectFormFactory = inlineformset_factory(Imovel, Attr)
    
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        
        
        if form.is_valid():
            imovel = form.save()
            
            formset = ObjectFormFactory(request.POST, instance=imovel)
            
            if formset.is_valid():
                attrs = formset.save()
                
                os.makedirs(os.path.join(STATICFILES_DIRS[0], "extras", str(imovel.id), "docs"))
                os.makedirs(os.path.join(STATICFILES_DIRS[0], "extras", str(imovel.id), "fotos"))
    
                return HttpResponseRedirect(reverse('imoveis.views.docs', args=(imovel.id,)))
    
    else:
        form = ImovelForm()        
        formset = ObjectFormFactory()

    response = render_to_response("imoveis/add.html",
                                 { 
                                  "module":MODULE+"> Adicionar ",
                                  "form": form,
                                  "formset": formset,
                                  },
                                  request
                                 )
    return response


@login_required   
def delete(request, object_id, assertion="n"):
    object = Imovel.objects.get(pk=object_id)
    
    if str(assertion).lower() == "s":   
        # Remove as pastas com os documentos e fotos do imóvel
        shutil.rmtree(os.path.join(STATICFILES_DIRS[0], "extras", str(object.id)), ignore_errors=True)
        
        object.delete()
        return HttpResponseRedirect(reverse('imoveis.views.list'))
    
    else:
        response = render_to_response("imoveis/delete.html",
                                      {
                                       "module":MODULE+"> Deletar ",
                                       "imovel":object,
                                       },
                                      request
                                      )
    return response


@login_required
def docs(request, object_id):
    R_DOCS_PATH = os.path.join(STATICFILES_DIRS[0], "extras", object_id, "docs")
    R_IMG_PATH = os.path.join(STATICFILES_DIRS[0], "extras", object_id, "fotos")
    D_DOCS_PATH = "/static/extras/%s/docs" %(object_id)
    D_IMG_PATH = "/static/extras/%s/fotos" %(object_id)
    
    img_count = os.listdir(R_IMG_PATH).__len__()
    
    if request.method == 'POST':
        up_files =  request.FILES.getlist('fileX[]')
        for file in up_files:        
            
            filename = str(file)
            if re.search("\.(jpg|gif|png|img|bmp|JPG|GIF|PNG|IMG|BMP)$", filename) != None:
                path = R_IMG_PATH
                
            else:
                path = R_DOCS_PATH
            
            fd = open('%s/%s' % (path, filename), 'wb')
            fd.write(file.read())
            fd.close()
    
    docs_list = os.listdir(R_DOCS_PATH)
    
    docs_dict = {}
    for dn in docs_list:
        docs_dict[dn] = D_DOCS_PATH+"/%s" %(dn)
        
    img_list = os.listdir(R_IMG_PATH)
    
    for i in img_list:
        if re.search("\.(jpg|gif|png|img|bmp|JPG|GIF|PNG|IMG|BMP)$", i) == None:
            img_list.remove(i)
                
    for i in range(len(img_list)):
        img_list[i] = "%s/%s" %(D_IMG_PATH, img_list[i])
    
    response = render_to_response("imoveis/docs.html",
                                  {
                                   "module":MODULE+"> Docs ",
                                   "docs_dict":docs_dict,
                                   "img_list":img_list,
                                   },
                                  request
                                  )
    return response


@login_required
def match(inst):
    model = clientes_models.Comprador
    
    query = make_match(inst, model)
    
    match_list = model.objects.filter(query)
    
    response = render_to_response("match.html",
                                  {
                                   "module": "> Match",
                                   "match_list":match_list,
                                   },
                                  inst
                                  )
    return response
