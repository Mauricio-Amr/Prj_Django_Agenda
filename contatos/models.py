# type : ignore
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'

    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nome}'


class Contato(models.Model):

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='imagem/%Y/%m')
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
