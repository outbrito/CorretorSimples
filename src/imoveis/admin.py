from imoveis.models import *
from django.contrib import admin


class M_AttrInline(admin.TabularInline):
    model = M_Attr
    
class AttrInline(admin.TabularInline):
    model = Attr

admin.site.register(M_Class, inlines=(M_AttrInline,))
admin.site.register(Imovel, inlines=(AttrInline,))
#admin.site.register(M_Attribute)
#admin.site.register(Attr)
