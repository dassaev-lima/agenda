from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao','status')
    list_filter = ('titulo','usuario','data_evento',)

# Register your models here.
admin.site.register(Evento,EventoAdmin)