from typing import Any
from django.db import models

# Create your models here.
class Categoria(models.Model):
  nombre= models.CharField(max_length=100)
  pub_date= models.DateField('fecha de registro', auto_now=True)

  def __str__(self):
    return self.nombre

class Producto(models.Model):
  categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
  nombre= models.CharField(max_length=100)
  precio= models.DecimalField(max_digits=6, decimal_places=2)
  stock= models.IntegerField(default=0)
  upload = models.TextField(null= True) 
  pub_date= models.DateField('date published')

  def __str__(self):
    return self.nombre
