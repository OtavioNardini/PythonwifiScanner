from django.db import models
import json

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, default='sem-email@example.com')
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class WifiScan(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='wifi_scans')
    data_hora = models.DateTimeField(auto_now_add=True)
    redes = models.JSONField(default=list)  # Salva a lista de redes em JSON
    total_networks = models.IntegerField(default=0)
    avg_signal = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-data_hora']
    
    def __str__(self):
        return f"Scan de {self.usuario.nome} - {self.data_hora}"