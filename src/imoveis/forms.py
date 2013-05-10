# -*- coding: UTF-8 -*-

'''
Created on 10/05/2013

@author: ThiagoP
'''

# Python Imports
from datetime import date
# Django Imports
from django import forms
# Project Imports
from models import Imovel
from html5forms.fields import Html5DateField


class ImovelForm(forms.ModelForm):
    data_cadastro = Html5DateField(initial=date.today)
    data_negocio = Html5DateField(required=False)

    class Meta:
        model = Imovel