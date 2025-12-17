from django.contrib import admin
from .models import Usuario, WifiScan

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(WifiScan)
class WifiScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_hora', 'total_networks', 'avg_signal')
    search_fields = ('usuario__nome',)
    list_filter = ('data_hora',)
    readonly_fields = ('data_hora', 'redes', 'total_networks', 'avg_signal')

