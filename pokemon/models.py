from django.db import models
from django.contrib.auth.models import User

class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Pokemon(models.Model):
    TIPOS = [
        ('F', 'Fuego'),
        ('A', 'Agua'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    fotografia = models.ImageField(upload_to='pokemons/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre