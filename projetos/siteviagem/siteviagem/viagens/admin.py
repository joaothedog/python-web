from django.contrib import admin
from .models import Viagem, Passageiro, GastoExtra

admin.site.register(Viagem)
admin.site.register(Passageiro)
admin.site.register(GastoExtra)