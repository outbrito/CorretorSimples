from django.db.models import Q

def make_match(instance, cls):
    query_f = Q(valor__lte=instance.valor, negocio=instance.negocio)
    
    query = Q()
    for i in instance._meta.fields:
        field_names = [field.name for field in cls._meta.fields]
        
        
        
        if i.name in field_names:
#            print i.name
            if instance.__getattribute__(i.name) == None or instance.__getattribute__(i.name) == "":
                continue
            
            if i.name == "endereco":
                query.add(Q(endereco__icontains=instance.endereco), Q.OR)
            if i.name == "bairro":
                query.add(Q(bairro__icontains=instance.bairro), Q.OR)     
            if i.name == "cidade":
                query.add(Q(cidade__icontains=instance.cidade), Q.OR)     
            if i.name == "estado":
                query.add(Q(estado__icontains=instance.estado), Q.OR)                  
            if i.name == "quartos":
                query.add(Q(quartos=instance.quartos), Q.OR)               
            if i.name == "suites":
                query.add(Q(suites=instance.suites), Q.OR)                
            if i.name == "salas":
                query.add(Q(salas=instance.salas), Q.OR)                 
            if i.name == "banheiros":
                query.add(Q(banheiros=instance.banheiros), Q.OR)             
            if i.name == "lavabos":
                query.add(Q(lavabos=instance.lavabos), Q.OR)               
            if i.name == "closet":
                query.add(Q(closet=instance.closet), Q.OR)                
            if i.name == "dce":
                query.add(Q(dce=instance.dce), Q.OR)                   
            if i.name == "hidro":
                query.add(Q(hidro=instance.hidro), Q.OR)                 
            if i.name == "terraco":
                query.add(Q(terraco=instance.terraco), Q.OR)               
            if i.name == "varanda":
                query.add(Q(varanda=instance.varanda), Q.OR)               
            if i.name == "copa_cozinha":
                query.add(Q(copa_cozinha=instance.copa_cozinha), Q.OR)          
            if i.name == "armarios_cozinha":
                query.add(Q(armarios_cozinha=instance.armarios_cozinha), Q.OR)      
            if i.name == "armarios_quarto":
                query.add(Q(armarios_quarto=instance.armarios_quarto), Q.OR)       
            if i.name == "area_servico":
                query.add(Q(area_servico=instance.area_servico), Q.OR)          
            if i.name == "piscina":
                query.add(Q(piscina=instance.piscina), Q.OR)               
            if i.name == "salao_festas":
                query.add(Q(salao_festas=instance.salao_festas), Q.OR)          
            if i.name == "salao_jogos":
                query.add(Q(salao_jogos=instance.salao_jogos), Q.OR)           
            if i.name == "sauna":
                query.add(Q(sauna=instance.sauna), Q.OR)                 
            if i.name == "mezanino":
                query.add(Q(mezanino=instance.mezanino), Q.OR)              
            if i.name == "vagas_garagem":
                query.add(Q(vagas_garagem=instance.vagas_garagem), Q.OR)         
            if i.name == "laje_plana":
                query.add(Q(laje_plana=instance.laje_plana), Q.OR)            
            if i.name == "quintal":
                query.add(Q(quintal=instance.quintal), Q.OR)               
            if i.name =="jardim":
                query.add(Q(jardim=instance.jardim), Q.OR)                
            if i.name == "area":
                query.add(Q (area=instance.area, un=instance.un) , Q.OR)     
            if i.name == "area_total": 
                query.add( Q(area_total=instance.area_total, un=instance.un), Q.OR)     
            if i.name == "posicao":
                query.add(Q(posicao=instance.posicao), Q.OR)               
            if i.name == "andar":
                query.add(Q(andar=instance.andar), Q.OR)                 
            if i.name == "edificio":
                query.add(Q(edificio=instance.edificio), Q.OR)              
            if i.name == "elevadores":
                query.add(Q(elevadores=instance.elevadores), Q.OR)            
            if i.name == "guarita":
                query.add(Q(guarita=instance.guarita), Q.OR)               
            if i.name == "central_gas":
                query.add(Q(central_gas=instance.central_gas), Q.OR)           
            if i.name == "gerador":
                query.add(Q(gerador=instance.gerador), Q.OR)               
            if i.name == "area_lazer":
                query.add(Q(area_lazer=instance.area_lazer), Q.OR)            
            if i.name == "garagem":
                query.add(Q(garagem=instance.garagem), Q.OR)
                
    query_f.add(query, Q.AND)
    
    return query_f
