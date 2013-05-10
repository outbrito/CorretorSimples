from django.db.models import Q

def make_query(param):
    query = (
             Q(nome__icontains=param)   |
             Q(tel__icontains=param)    |
             Q(cell__icontains=param)
             )
    
    return query

#def make_match(instance):
#    for field in model._meta.fields:
#    query = (
#             Q(endereco__icontains=Comprador_or_Imovel.endereco)   |
#             Q(bairro__icontains=Comprador_or_Imovel.bairro)     |
#             Q(cidade__icontains=Comprador_or_Imovel.cidade)     |
#             Q(estado__icontains=Comprador_or_Imovel.estado)     |
#             Q(valor__lt=Comprador_or_Imovel.valor)             |
#             Q(quartos=Comprador_or_Imovel.quartos)               |
#             Q(suites=Comprador_or_Imovel.suites)                |
#             Q(salas=Comprador_or_Imovel.salas)                 |
#             Q(banheiros=Comprador_or_Imovel.banheiros)             |
#             Q(lavabos=Comprador_or_Imovel.lavabos)               |
#             Q(closet=Comprador_or_Imovel.closet)                |
#             Q(dce=Comprador_or_Imovel.dce)                   |
#             Q(hidro=Comprador_or_Imovel.hidro)                 |
#             Q(terraco=Comprador_or_Imovel.terraco)               |
#             Q(varanda=Comprador_or_Imovel.varanda)               |
#             Q(copa_cozinha=Comprador_or_Imovel.copa_cozinha)          |
#             Q(armarios_cozinha=Comprador_or_Imovel.armarios_cozinha)      |
#             Q(armarios_quarto=Comprador_or_Imovel.armarios_quarto)       |
#             Q(area_servico=Comprador_or_Imovel.area_servico)          |
#             Q(piscina=Comprador_or_Imovel.piscina)               |
#             Q(salao_festas=Comprador_or_Imovel.salao_festas)          |
#             Q(salao_jogos=Comprador_or_Imovel.salao_jogos)           |
#             Q(sauna=Comprador_or_Imovel.sauna)                 |
#             Q(mezanino=Comprador_or_Imovel.mezanino)              |
#             Q(vagas_garagem=Comprador_or_Imovel.vagas_garagem)         |
#             Q(laje_plana=Comprador_or_Imovel.laje_plana)            |
#             Q(quintal=Comprador_or_Imovel.quintal)               |
#             Q(jardim=Comprador_or_Imovel.jardim)                |
#             (Q(area=Comprador_or_Imovel.area) & Q(un=Comprador_or_Imovel.un))     |
#             (Q(area_total=Comprador_or_Imovel.area_total)& Q(un=Comprador_or_Imovel.un))     |
#             Q(posicao=Comprador_or_Imovel.posicao)               |
#             Q(andar=Comprador_or_Imovel.andar)                 |
#             Q(edificio=Comprador_or_Imovel.edificio)              |
#             Q(elevadores=Comprador_or_Imovel.elevadores)            |
#             Q(guarita=Comprador_or_Imovel.guarita)               |
#             Q(central_gas=Comprador_or_Imovel.central_gas)           |
#             Q(gerador=Comprador_or_Imovel.gerador)               |
#             Q(area_lazer=Comprador_or_Imovel.area_lazer)            |
#             Q(garagem=Comprador_or_Imovel.garagem)
#             )
#    for i in instance._meta.fields:
#        print i.name
#    
#    return query