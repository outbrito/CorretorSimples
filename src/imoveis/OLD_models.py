# -*- coding: UTF-8 -*-

from django.db import models
from time import strftime

from clientes.models import *


__all__ = ["Casa", "Apartamento", "Flat", "Terreno", "Granja", "Chacara", "Fazenda", "Hotel", "Pousada", "Loja", "Sala", "Galpao", "Cobertura", "Duplex", "Outros"]

ESTRUTURAS = ((1,"Sub Pilotis"),(2,"Caixão"))
UNIDADES = ((1,"m2"),(2,"hec"))
NEGOCIACAO = ((1,"VENDA"),(2,"ALUGUEL"), (3,"ALUGUEL DE TEMPORADA"), (4,"PERMUTA"))



# Modelos de imóveis
class Imovel(models.Model):
    #Dados da venda
    negocio = models.IntegerField("Negociação", choices=NEGOCIACAO)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data_cadastro = models.DateField("Data do Cadastro", default=strftime("%d/%m/%Y"))
    data_negocio = models.DateField("Data da Negociação", null=True, blank=True)
    negocio_externa = models.BooleanField("Negociação Externa", default=False)
    obs_negocio = models.TextField("Informações da Negociação", blank=True)
    
    #Dados do imóvel (junto com características das classes)   
    proprietario = models.ManyToManyField(Proprietario)
    endereco = models.CharField("Endereço", max_length=100)
    bairro = models.CharField("Bairro", max_length=100)
    referencia = models.TextField("Ponto de Referência", blank=True)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=2, default="PB")
    url_santana = models.URLField("'santanacimoveis.com.br'", verify_exists=False, blank=True)
    url_mostra = models.URLField("'mostraimoveis.com.br'", verify_exists=False, blank=True)
    cod_jornal = models.IntegerField("Código no Jornal")
    obs = models.TextField("Observações", blank=True)
    
    
    
    def __str__(self):
        return self.__class__.__name__+" na "+self.endereco
    
    def get_absolute_url(self):
        return "/CORRETOR/imoveis/%s/%i" %(self.__class__.__name__, self.id)        
     
    class Meta:
        abstract = True
   

class Moradia(Imovel):
    quartos = models.IntegerField("Quartos")
    suites = models.IntegerField("Suítes")
    salas = models.CharField("Salas", max_length=100)
    wc = models.IntegerField("WC's")
    lavabos = models.IntegerField("Lavabos")
    closet = models.BooleanField("Closet")
    dce = models.BooleanField("DCE")
    hidro = models.BooleanField("Hidromassagem")
    terraco = models.CharField("Terraço", max_length=100)
    varanda = models.IntegerField("Varanda")
    copa_cozinha = models.BooleanField("Copa/Cozinha")
    armarios_cozinha = models.BooleanField("Armarios de Cozinha")
    armarios_quarto = models.BooleanField("Armarios no Quarto")
    area_servico = models.BooleanField("Área de Serviço")
    piscina = models.BooleanField("Piscina")
    salao_festas = models.BooleanField("Salão de Festas")
    salao_jogos = models.BooleanField("Salão de Jogos")
    sauna = models.BooleanField("Sauna")
    mezanino = models.BooleanField("Mezanino")
    vagas_garagem = models.IntegerField("Vagas na Garagem")
    area = models.FloatField("Área Construída")
    area_total = models.FloatField("Área Total")
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1)
    posicao = models.CharField("Posição", max_length=100)
    
    class Meta:
        abstract = True
    

class Casa(Moradia):
    laje_plana = models.BooleanField("Laje Plana")
    quintal = models.BooleanField("Quintal")
    jardim = models.BooleanField("Jardim")
    

class Duplex(Casa):
    class Meta:
        verbose_name = "Duplex"
        verbose_name_plural = "Duplexes"
        

class Pousada(Casa):
    pass
        

class Apartamento(Moradia):
    numero = models.IntegerField("Apartamento Nº")
    andar = models.IntegerField("Andar")
    edificio = models.CharField("Edificio", max_length=100)
    andares = models.IntegerField("Andares")
    elevadores = models.IntegerField("Nº de Elevadores")
    guarita = models.BooleanField("Guarita")
    central_gas = models.BooleanField("Central de Gás")
    gerador = models.BooleanField("Gerador")
    area_lazer = models.BooleanField("Área de Lazer")
    garagem = models.IntegerField("Estrutura", choices=ESTRUTURAS)


class Cobertura(Apartamento):
    pass
    

class Flat(Apartamento):
    pass


class Hotel(Apartamento):
    class Meta:
        verbose_name_plural = "Hotéis"
        
        
class Terreno(Imovel):
    area_total = models.FloatField("Área Total")
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1)


class Granja(Moradia):
    pass


class Chacara(Granja):
    class Meta:
        verbose_name = "Chácara"
        verbose_name_plural = "Chácaras"


class Fazenda(Granja):
    pass


class Sala(Imovel):
    area = models.FloatField("Área Construída")
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1)
    posicao = models.CharField("Posição", max_length=100)
    area_total = models.FloatField("Área Total")

class Loja(Sala):
    pass


class Galpao(Imovel):
    area = models.FloatField("Área Construída")
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1)
    posicao = models.CharField("Posição", max_length=100)
    area_total = models.FloatField("Área Total")
    
    class Meta:
        verbose_name = "Galpão"
        verbose_name_plural = "Galpões"

        
class Outros(models.Model):
    #Dados da venda
    negocio = models.IntegerField("Negociação", choices=NEGOCIACAO)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data_cadastro = models.DateField("Data do Cadastro", default=strftime("%d/%m/%Y"))
    data_negocio = models.DateField("Data da Negociação", null=True, blank=True)
    negocio_externa = models.BooleanField("Negociação Externa", default=False)
    obs_negocio = models.TextField("Informações da Negociação", blank=True)
    
    #Dados do imóvel (junto com características das classes)
    tipo_imovel = models.CharField("Tipo do Imóvel", max_length=100)   
    proprietario = models.ManyToManyField(Proprietario)
    endereco = models.CharField("Endereço", max_length=100)
    bairro = models.CharField("Bairro", max_length=100)
    referencia = models.TextField("Ponto de Referência", blank=True)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=2, default="PB")
    url_santana = models.URLField("'santanacimoveis.com.br'", verify_exists=False, blank=True)
    url_mostra = models.URLField("'mostraimoveis.com.br'", verify_exists=False, blank=True)
    cod_jornal = models.IntegerField("Código no Jornal")
    
    area = models.FloatField("Área Construída")
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1)
    posicao = models.CharField("Posição", max_length=100)
    area_total = models.FloatField("Área Total")
    
    obs = models.TextField("Observações", blank=True)
    
    def __str__(self):
        return self.tipo_imovel+" na "+self.endereco
    
    def get_absolute_url(self):
        return "/CORRETOR/imoveis/%s/%i" %(self.__class__.__name__, self.id)
    
    class Meta:
        verbose_name = "Outros"
        verbose_name_plural = "Outros"
