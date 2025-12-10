from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, default='sem-email@example.com')
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome