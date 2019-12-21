from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Director(models.Model):
    nombre= models.CharField(max_length=50, verbose_name="Director", blank=False, null=False)
    birth= models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    nacion= models.CharField(max_length=25, verbose_name="Nacionalidad", blank=True, null=True)
    def __str__(self):
        return u'%s' % (self.nombre)

class Actor(models.Model):
    nombre= models.CharField(max_length=50, verbose_name="Actor", blank=False, null=False)
    birth= models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    nacion= models.CharField(max_length=25, verbose_name="Nacionalidad", blank=True, null=True)
    foto= models.URLField(verbose_name="Foto")
    def __str__(self):
        return u'%s' % (self.nombre)

class Pelicula(models.Model):
    titulo= models.CharField(max_length=100, verbose_name="Título", blank=False,null=False)
    tituloAlt= models.CharField(max_length=100, verbose_name="a.k.a", blank=False,null=False)
    anno= models.PositiveIntegerField(default=1888,verbose_name="Año", blank=True, null=True,validators=[MinValueValidator(1888)])
    director= models.ForeignKey(Director, on_delete=models.CASCADE, blank=True, null=True)
    #actor= models.ManyToManyField(Actor)
    actor= models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True, null=True)
    genero= models.CharField(max_length=100, verbose_name="Género", blank=True, null=True)
    cover= models.URLField(verbose_name="Portada")
    def __str__(self):
        return u'%s' % (self.titulo)
###############################################################################################
