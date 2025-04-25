from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Residencial, Apartamento, Morador, Contrato, Manutencao, Pagamento

# Personalização da interface admin
admin.site.site_header = "JP Imobiliaria"
admin.site.site_title = "Painel Administrativo"
admin.site.index_title = "Gerenciamento do Sistema"

# Registro dos modelos no admin
admin.site.register(Residencial)
admin.site.register(Apartamento)
admin.site.register(Morador)
admin.site.register(Contrato)
admin.site.register(Manutencao)
admin.site.register(Pagamento)
