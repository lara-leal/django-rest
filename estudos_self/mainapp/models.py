from django.db import models

class Diretor(models.Model):
 nome = models.CharField(max_length=255)
 bestMovie = models.CharField(max_length=255)
 email = models.EmailField()
 
class Filme(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    dataLancamento = models.DateField()
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    bilheteria = models.PositiveIntegerField()
    
class Ator(models.Model):
    nome = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    bestMovie = models.CharField(max_length=255)