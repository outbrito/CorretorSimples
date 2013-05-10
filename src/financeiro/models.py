# -*- coding: UTF-8 -*-

from django.db import models

__all__ = ["Pagamento", "Recebimento"]

#Modelos financeiros
class _Movimento(models.Model):
    referencia = models.CharField("Referência", max_length=100)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    vencimento = models.DateField("Vencimento")
    pago = models.BooleanField("Pago")
    data_pagamento = models.DateField("Data do Pagamento", null=True, blank=True)
    
    def __str__(self):
        return self.__class__.__name__ +" "+ self.referencia
    
    def get_absolute_url(self):
        return "/CORRETOR/financeiro/%s/%i" %(self.__class__.__name__, self.id)
    
    class Meta:
        abstract = True

class Pagamento(_Movimento):
    pass

class Recebimento(_Movimento):
    devedor = models.CharField("Devedor", max_length=100)
    contato = models.CharField("Contato", max_length=12)