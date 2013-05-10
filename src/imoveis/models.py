# -*- coding: UTF-8 -*-

'''
Created on 27/07/2010

@author: ThiagoP
'''

from django.db import models
from time import strftime

from clientes.models import Proprietario

DATATYPES = ((1,'INT'), (2,'FLOAT'), (3,'STRING'))

ESTRUTURAS = ((1,"Sub Pilotis"),(2,"Caixão"))
UNIDADES = ((1,"m2"),(2,"hec"))
NEGOCIACAO = ((1,"VENDA"),(2,"ALUGUEL"), (3,"ALUGUEL DE TEMPORADA"), (4,"PERMUTA"))
    


# Modelos de objetos
class M_Class(models.Model):
    classe = models.CharField("Classe", max_length=20)
    
    def __str__(self):
        return self.classe
    
    class Meta:
        verbose_name_plural = "M_Classes"



class M_Attr(models.Model):
    m_class = models.ForeignKey(M_Class, verbose_name="Classe")
    tipo = models.IntegerField("Tipo", choices=DATATYPES, max_length=20)
    nome = models.CharField("Nome do Atributo", max_length=20)
    mascara = models.CharField("Mascara", max_length=100, null=True, blank=True)
    obrigatorio = models.BooleanField("Obriga Resposta", default=False)
    
    def __str__(self):
        return self.nome


class Imovel(models.Model):
    #Dados da venda
    proprietario = models.ManyToManyField(Proprietario)
    m_imovel = models.ForeignKey(M_Class, verbose_name="Tipo de Imóvel")
    negocio = models.IntegerField("Negociação", choices=NEGOCIACAO)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data_cadastro = models.DateField("Data do Cadastro")
    data_negocio = models.DateField("Data da Negociação", null=True, blank=True)
    negocio_externa = models.BooleanField("Negociação Externa", default=False)
    obs_negocio = models.TextField("Informações da Negociação", blank=True)
    
    #Dados do imóvel (junto com características das classes)   
    endereco = models.CharField("Endereço", max_length=100)
    bairro = models.CharField("Bairro", max_length=100)
    referencia = models.TextField("Ponto de Referência", blank=True)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=2, default="PB")
#    url_santana = models.URLField("'santanacimoveis.com.br'", blank=True)
#    url_mostra = models.URLField("'mostraimoveis.com.br'", blank=True)
    cod_jornal = models.CharField("Código no Jornal", max_length=20, null=True, blank=True)
    obs = models.TextField("Observações", blank=True)
    
    
    def __str__(self):
        ret = self.m_imovel.classe.upper() + " End: " + self.endereco
        return ret
    
    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
        
        
        
class Attr(models.Model):
    m_attr = models.ForeignKey(M_Attr, verbose_name="Tipo de Atributo")
    valor = models.CharField("Valor", max_length=500)
    imovel = models.ForeignKey(Imovel)
    
    def __str__(self):
        s_ret = self.m_attr.nome+ ": " + self.valor
        return s_ret 
    
    class Meta:
        verbose_name = "Attribute"
        unique_together = [("m_attr", "imovel")]
        ordering = ['m_attr']
        

    
