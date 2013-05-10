from django.db.models import Q

def make_query(param):
    query = (
             Q(endereco__icontains=param)   |
             Q(bairro__icontains=param)     |
             Q(cidade__icontains=param)     |
             Q(estado__icontains=param)     |
             Q(obs__icontains=param)        |
             Q(valor__lt=param)             |
             Q(data_cadastro__iexact=param) |
             Q(data_venda__iexact=param)
             )
    
    return query