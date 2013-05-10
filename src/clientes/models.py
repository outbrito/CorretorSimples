# -*- coding: UTF-8 -*-

from django.db import models


__all__ = ["Proprietario","Comprador"]

TIPO = ((0, 'Casa'), (1, 'Apartamento'), (2, 'Flat'), (3, 'Terreno'), (4, 'Granja'), (5, 'Chacara'), (6, 'Fazenda'), (7, 'Hotel'), (8, 'Pousada'), (9, 'Loja'), (10, 'Sala'), (11, 'Galpao'), (12, 'Cobertura'), (13, 'Duplex'), (14, "Outros") )
ESTRUTURAS = ((1,"Sub Pilotis"),(2,"Caixão"))
UNIDADES = ((1,"m2"),(2,"hec"))
NEGOCIACAO = ((1,"VENDA"),(2,"ALUGUEL"), (3,"ALUGUEL DE TEMPORADA"), (4,"PERMUTA"))



#Modelos de cliente
class _Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)
    tel = models.CharField("Telefone", max_length=12)
    cell = models.CharField("Celular", max_length=12)
    email = models.EmailField("E-mail", blank=True)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return "/clientes/%s/%i" %(self.__class__.__name__, self.id)
    
    class Meta:
        abstract = True

    
######################################################################################################    
class Proprietario(_Cliente):
    endereco = models.CharField("Endereço", max_length=100, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    estado = models.CharField("Estado", max_length=2, blank=True, null=True)
    
    class Meta:
        verbose_name = "Proprietário"
        verbose_name_plural = "Proprietários"


class Comprador(_Cliente):
    data_cadastro = models.DateField("Data do Cadastro", auto_now_add=True)
    
    tipo = models.IntegerField("Tipo", choices=TIPO)
    
    endereco = models.CharField("Endereço", max_length=100, blank=True, null=True)
    bairro = models.CharField("Bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    estado = models.CharField("Estado", max_length=100, blank=True, null=True)
    
    negocio = models.IntegerField("Negociação", choices=NEGOCIACAO)    
    valor = models.DecimalField("Valor", max_digits=20, decimal_places=2, blank=True, null=True)
    
    quartos = models.IntegerField("Quartos", blank=True, null=True)
    suites = models.IntegerField("Suítes", blank=True, null=True)
    salas = models.IntegerField("Salas", blank=True, null=True)
    banheiros = models.IntegerField("Banheiros", blank=True, null=True)
    lavabos = models.IntegerField("Lavabos", blank=True, null=True)
    closet = models.NullBooleanField("Closet", blank=True, null=True)
    dce = models.NullBooleanField("DCE", blank=True, null=True)
    hidro = models.NullBooleanField("Hidromassagem", blank=True, null=True)
    terraco = models.NullBooleanField("Terraço", blank=True, null=True)
    varanda = models.IntegerField("Varanda", blank=True, null=True)
    copa_cozinha = models.NullBooleanField("Copa/Cozinha", blank=True, null=True)
    armarios_cozinha = models.NullBooleanField("Armarios de Cozinha", blank=True, null=True)
    armarios_quarto = models.NullBooleanField("Armarios no Quarto", blank=True, null=True)
    area_servico = models.NullBooleanField("Área de Serviço", blank=True, null=True)
    piscina = models.NullBooleanField("Piscina", blank=True, null=True)
    salao_festas = models.NullBooleanField("Salão de Festas", blank=True, null=True)
    salao_jogos = models.NullBooleanField("Salão de Jogos", blank=True, null=True)
    sauna = models.NullBooleanField("Sauna", blank=True, null=True)
    mezanino = models.NullBooleanField("Mezanino", blank=True, null=True)
    vagas_garagem = models.IntegerField("Vagas na Garagem", blank=True, null=True)
    
    laje_plana = models.NullBooleanField("Laje", blank=True, null=True)
    quintal = models.NullBooleanField("Quintal", blank=True, null=True)
    jardim = models.NullBooleanField("Jardim", blank=True, null=True)
    
    area = models.FloatField("Área Construída", blank=True, null=True)
    un = models.IntegerField("Un de Área", max_length=3, choices=UNIDADES, default=1, blank=True, null=True)
    area_total = models.FloatField("Área Total", blank=True, null=True)
    
    posicao = models.CharField("Posição", max_length=100, blank=True, null=True)

    andar = models.IntegerField("Andar", blank=True, null=True)
    edificio = models.CharField("Edificio", max_length=100, blank=True, null=True)
    elevadores = models.IntegerField("Nº de Elevadores", blank=True, null=True)
    guarita = models.NullBooleanField("Guarita", blank=True, null=True)
    central_gas = models.NullBooleanField("Central de Gás", blank=True, null=True)
    gerador = models.NullBooleanField("Gerador", blank=True, null=True)
    area_lazer = models.NullBooleanField("Área de Lazer", blank=True, null=True)
    garagem = models.IntegerField("Estrutura", choices=ESTRUTURAS, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Compradores"
        

######################################################################################################