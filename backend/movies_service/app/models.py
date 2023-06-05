from django.db import models

# Create your models here.
class Movie(models.Model):
    nome = models.CharField(max_length=128)
    ano_lancamento = models.IntegerField()
    diretor = models.CharField(max_length=128)
    genero = models.CharField(max_length=50)
    globo_ouro = models.IntegerField()
    oscar = models.IntegerField()
    nota = models.FloatField()
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    