# -*- coding: UTF-8 -*-

from django import forms
from django.forms import ModelForm
from time import strftime

REPORTSQ = (("","---------"),(1,"Vendas Por Categoria"), (2,"Financeiro"), (3,"Cadastro de Imóveis"),(4,"Evolução de Vendas"), (5,"Evolução Financeira"), (6,"Evolução de Cadastros"))

formato_data = "%d/%m/%Y"


class FormReport(forms.Form):
    relatorio = forms.IntegerField(widget=forms.Select(choices=REPORTSQ))
    ano = forms.CharField(max_length=4, required=False)
    
#class FormReportEvol(forms.Form):
#    relatorio = forms.IntegerField(widget=forms.Select(choices=REPORTSEVOL))
#    
##    data_final = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'vDateField'}), required=False)
##    agrupamento = forms.IntegerField(widget=forms.Select(choices=GROUPMENT), required=False)

class CostumizedModelForm(ModelForm):
    vencimento = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'vDateField'}, format=formato_data), input_formats=[formato_data], label="Vencimento")
    data_pagamento = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'vDateField'}, format=formato_data), input_formats=[formato_data], required=False, label="Data de Pagamento")  
