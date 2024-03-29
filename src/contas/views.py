# -*- coding: utf-8 -*-

'''
Created on 18/04/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date, timedelta
# Django Imports
from django.shortcuts import render_to_response, RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Project Imports
from forms import FormPerfil, FormUsuario, FormRegistrar
from models import PerfilUsuario, Cidade, Estado


def registrar(request):
    if request.method == 'GET':
        form = FormRegistrar()
        ret = render_to_response("contas/registrar.html", {'form': form}, context_instance=RequestContext(request))
        
    elif request.method == 'POST':
        form = FormRegistrar(request.POST)
        
        if form.is_valid():
            user_form = form.save(commit=False)
            user = User.objects.create_user(username=user_form.username, password=user_form.password, email=user_form.email, first_name=user_form.first_name, last_name=user_form.last_name)
            perfil, true = PerfilUsuario.objects.get_or_create(usuario=user)
            
            user = authenticate(username=user_form.username, password=user_form.password)
            login(request, user)
    
            ret =  home(request)
        else:
            ret = render_to_response("contas/registrar.html", {'form': form}, context_instance=RequestContext(request))
        
    return ret
    
    
@login_required
def home(request):
    if request.method == 'POST':
        form_usuario = FormUsuario(request.POST)
        form_perfil = FormPerfil(request.POST)
        
        if form_usuario.is_valid() and form_perfil.is_valid():
            user = form_usuario.save(commit=False)
            perfil = form_perfil.save(commit=False)
            
            request.user.first_name = user.first_name
            request.user.last_name = user.last_name
            request.user.email = user.email
            request.user.save()
            
            try:
                perfil_usuario = request.user.perfil
            except PerfilUsuario.DoesNotExist:
                perfil_usuario = PerfilUsuario()
                perfil_usuario.usuario = request.user
                perfil_usuario.expiracao = date.today()
            
            perfil_usuario.endereco = perfil.endereco
            perfil_usuario.numero = perfil.numero
            perfil_usuario.cpf_cnpj = perfil.cpf_cnpj
            perfil_usuario.complemento = perfil.complemento
            perfil_usuario.cidade = perfil.cidade
            perfil_usuario.estado = perfil.estado
            perfil_usuario.estabelecimento = perfil.estabelecimento
            
            perfil_usuario.save()
             
            form_usuario = FormUsuario(instance=request.user)
            form_perfil = FormPerfil(instance=request.user.perfil)
            
            ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil, 'success': "Dados salvos com sucesso."}
            
        else:
            ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil, 'error': "Verifique os erros abaixo...\n"}
            
    else:
        form_usuario = FormUsuario(instance=request.user)
        try:
            form_perfil = FormPerfil(instance=request.user.perfil)
        except PerfilUsuario.DoesNotExist:
            form_perfil = FormPerfil()
            
        ret = {'form_usuario': form_usuario, 'form_perfil': form_perfil}
            
    return render_to_response("contas/home.html", ret, context_instance=RequestContext(request))
    

def pagamento(request):
    pass


def paypal_return(request):
    pass