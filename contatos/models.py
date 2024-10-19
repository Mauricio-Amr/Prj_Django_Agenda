from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='imagem/%Y/%m')

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
