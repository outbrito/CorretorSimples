from django.db.models import Q

def make_query(param):
    query = (
             Q(referencia__icontains=param)   |
             Q(valor=param)    |
             Q(vencimento=param)
             )

    return query