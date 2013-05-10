# -*- coding: UTF-8 -*-

'''
Created on 30/05/2009

@author: ThiagoP
'''

# Python Imports
import os
import datetime
import shutil
import tarfile
# Django Imports
from shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Project Imports
import manage, settings
from imoveis import models as imoveis_models
from clientes import models as clientes_models
from extras.model_match import make_match
from extras.simplebackup import BKP


MODULE = "> Home "

DIR_EXPORT = "F:/Desenv/CORRETOR/export"
DIR_IMPORT = "F:/Desenv/CORRETOR/import"


@login_required
def home(request, status=''):
    
    response = render_to_response("home.html",
                                  {"module":MODULE,
                                   "status":status,
                                   },
                                  request
                                  )
    return response


@login_required
def gerdata(request):
    try:
        import sys
        
        old = sys.stdout
        file = open(DIR_EXPORT+"/CORRETORdata.json", "w")
        sys.stdout = file
    
        manage.execute_manager(settings, ["manage.py", "dumpdata", "--format=json", "--indent=2"])
    
        sys.stdout = old
        file.close()

        tar = tarfile.open(DIR_EXPORT+"/extras.tar", "w")
        os.chdir("C:/CORRETOR/templates/extras")
        tar.add(".")
        tar.close()
        
        msg = 'Dados Gerados, faça a importação no Notebook...' 
    
    except:
        msg = "Erro na geração, entre em contato com o desenvolvedor (Thiago)."
    
    return main(request, msg)


@login_required
def impdata(request):
    try:
    	import urllib
    	
    	# Baixa o json
    	urllib.urlretrieve("http://localhost/CORRETOR/export/CORRETORdata.json", DIR_IMPORT+"/CORRETORdata.json")
    	
    	#Limpa a base pra evitar que imoveis ja deletados no server nao continuem aparecendo
    	manage.execute_manager(settings, ["manage.py", "reset", "--noinput", "clientes", "imoveis", "financeiro"])
    	manage.execute_manager(settings, ["manage.py", "loaddata", DIR_IMPORT+"/CORRETORdata.json"])
    	
    	
    	# Baixa fotos e documentos em um tarball
    	urllib.urlretrieve("http://localhost/CORRETOR/export/extras.tar", DIR_IMPORT+"/extras.tar")
    	
    	# Remove a pasta extras e descompacta o tarball atualizado nela
    	shutil.rmtree("F:/Desenv/CORRETOR/templates/extras/")
    	tar = tarfile.open(DIR_IMPORT+"/extras.tar", "r")
    	tar.extractall("F:/Desenv/CORRETOR/templates/extras")
    	tar.close()
    	
    	
    	msg = "Importação Realizada com Sucesso!!!"
    except:
		msg = "Erro na Importação, gere os dados e tente importar novamente ou entre em contato com o Desenvolvedor (Thiago)."
	
    return main(request, msg)