# -*- coding: UTF-8 -*-

import os, sys
from threading import Thread
import manage, settings



#os.system("tskill python")
#manage.py dumpdata/loaddata

def Deployer():
#    def run(self):
##        os.system("python manage.py syncdb")
##        os.system("python manage.py runserver")
        manage.execute_manager(settings, ["manage.py", "syncdb"])
        manage.execute_manager(settings, ["manage.py", "runserver"])
        

def nav():
    os.system("\"c:/arquivos de programas/mozilla firefox/firefox.exe\" http://localhost:8000")
        
def new_app():
    app = raw_input("Digite o nome da nova aplicação: ")
    os.system("python \"c:/Python26/Scripts/django-admin.py\" startapp "+app)

def kill():
    os.system("tskill python")


######################### Operacional #############################    
op = None
    
while True:
    print("\n------------------------------")
    print("Utilitario de projeto Django.")
    print("Escolha a opção desejada: ")
    print("1 - Sincronizar banco e fazer Deploy (http://localhost:8000)")
    print("2 - Chamar navegador na URL do projeto")
    print("3 - Criar nova aplicação")
    print("4 - Matar processos Python")
    print("\n0 - Sair")
    op = int(raw_input())
    print repr(op)   
    
    
    if op == 1:
        Deployer()
#        srv.start()
    elif op == 2:
        nav()
    elif op == 3:
        new_app()
    elif op == 4:
        kill()
    
    elif op == 0:
        kill()
        break
    else:
        print ("Opção Inválida!")
