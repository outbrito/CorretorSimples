# -*- coding: UTF-8 -*-
#!/usr/bin/python


from filecmp import dircmp
from os import path,remove
import shutil, time, sys

IGNORE = []
def BKP(source, destiny):
    comp = dircmp(source, destiny)
    
    print("Copiando arquivos do diretório \"%s\"\n\n" %(source))
    print(comp.report())
    print("\n\n")
    
    # Copia aquivos
    for i in comp.left_only:
        if i.lower() in IGNORE:
            continue
        
        elif(path.isdir(source+"/"+i+"/") == True):
            shutil.copytree(source+"/"+i+"/", destiny+"/"+i+"/")
        
        else:
            shutil.copy2(source+"/"+i, destiny)
    
    # Faz a busca recursiva de arquivos diferentes em diretórios que já existem
    for i in comp.common_dirs:
        BKP(source+"/"+i+"/", destiny+"/"+i+"/")

    # Exclui arquivos no backup que não estão mais no flashdrive
    for i in comp.right_only:
        if i.lower() in IGNORE:
            continue
        
        elif(path.isdir(destiny+"/"+i+"/") == True):
            shutil.rmtree(destiny+"/"+i+"/")
        
        else:
            remove(destiny+"/"+i)        

    print("\n\nConcluido!")
