#-*- coding: UTF-8 -*-

from django.http import HttpResponse
from time import strftime

from extras import report_generator
from clientes import models as clientes_models
from imoveis import models as imoveis_models
from financeiro import models as financeiro_models


OUTDIR = 'C:/CORRETOR/templates/IMG/relatorios/'



#===============================================================================
def __check_dates(data_inicial, data_final):
    if data_inicial == "" or data_inicial == None:
        data_inicial = "2000-01-01"
    if data_final == "" or data_final == None:
        data_final = strftime("%Y-%m-%d")
        
    return data_inicial, data_final
#===============================================================================


def VendasPorCategoria(year):
    if year == "":
        year = strftime("%Y")
    
    cs_list = [imoveis_models.__getattribute__(cs) for cs in imoveis_models.__all__]
    
    data = []
    for cs in cs_list:
        data.append( cs.objects.filter(data_negocio__isnull=False, data_negocio__year=year).count() )
        
    data = [tuple(data)]
    labels = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Vendas Por Categoria"
    
    drw = report_generator.getbarchart(title, data, {"min":0,"max":50, "step":5}, labels) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='VCchart')
    
    return "/site_media/IMG/relatorios/VCchart.gif"
    
def Financeiro(year):
    if year == "":
        year = strftime("%Y")
        
    cs_list = [financeiro_models.__getattribute__(cs) for cs in financeiro_models.__all__]
    
    pagas = []
    pendentes = []
    cadastradas = []
    for cs in cs_list:
        pagas.append( cs.objects.filter(pago=True).count() )
        pendentes.append( cs.objects.filter(pago=False).count() )
        cadastradas.append( cs.objects.filter().count() )
        
    data = [tuple(pagas), tuple(pendentes), tuple(cadastradas)]
    labels = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Financeiro"
    
    drw = report_generator.getbarchart(title, data, {"min":0,"max":50, "step":5}, labels, ["Pagas","Pendentes","Total"]) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='Fchart')
    
    return "/site_media/IMG/relatorios/Fchart.gif"
    
def CadastroImoveis(year):
    if year == "":
        year = strftime("%Y")
    
    cs_list = [imoveis_models.__getattribute__(cs) for cs in imoveis_models.__all__]
    
    data = []
    for cs in cs_list:
        data.append( cs.objects.count() )
        
    data = [tuple(data)]
    labels = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Cadastro de Imóveis"
    
    drw = report_generator.getbarchart(title, data, {"min":0,"max":100,"step":5}, labels) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='CIchart')
    
    return "/site_media/IMG/relatorios/CIchart.gif"


def EvolucaoVendasPorCategoria(year):
    if year == "":
        year = strftime("%Y")
        
    cs_list = [imoveis_models.__getattribute__(cs) for cs in imoveis_models.__all__]
    
    data = []
    for cs in cs_list:
        qs = cs.objects.filter(data_negocio__year=year)
        
        qs_group = []
        for i in range(1,13):
            qs_group.append( qs.filter(data_negocio__month=i).count() ) 
        
        data.append( tuple(qs_group) )
        
    legends = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Evolução de Vendas Por Categoria"
    labels = "Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez".split(" ")
    
    drw = report_generator.getlinechart(title, data, {"min":0,"max":50,"step":5}, labels, legends) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='EVchart')
    
    return "/site_media/IMG/relatorios/EVchart.gif"

def EvolucaoFinanceira(year):
    if year == "":
        year = strftime("%Y")
        
    cs_list = [financeiro_models.__getattribute__(cs) for cs in financeiro_models.__all__]
    
    data = []
    for cs in cs_list:
        qs = cs.objects.filter(vencimento__year=year)
        
        qs_group = []
        for i in range(1,13):
            nqs = qs.filter(vencimento__month=i)
            
            valor_total = 0
            for i in nqs:
                valor_total = valor_total + float(i.valor)
                
            qs_group.append(valor_total) 
        
        data.append( tuple(qs_group) )
        
    legends = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Evolução Financeira"
    labels = "Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez".split(" ")
    
    drw = report_generator.getlinechart(title, data, {"min":0,"max":10000,"step":1000}, labels, legends) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='EFchart')
    
    return "/site_media/IMG/relatorios/EFchart.gif"

def EvolucaoCadastroImoveis(year):
    if year == "":
        year = strftime("%Y")
        
    cs_list = [imoveis_models.__getattribute__(cs) for cs in imoveis_models.__all__]
    
    data = []
    for cs in cs_list:
        qs = cs.objects.filter(data_cadastro__year=year)
        
        qs_group = []
        for i in range(1,13):
            qs_group.append( qs.filter(data_cadastro__month=i).count() ) 
        
        data.append( tuple(qs_group) )
        
    legends = [cs._meta.verbose_name.capitalize() for cs in cs_list]
    title = "Evolução do Cadastro de Imóveis"
    labels = "Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez".split(" ")
    
    drw = report_generator.getlinechart(title, data, {"min":0,"max":50,"step":5}, labels, legends) 
    
    drw.save(formats=['gif'],outDir=OUTDIR,fnRoot='EVchart')
    
    return "/site_media/IMG/relatorios/EVchart.gif"