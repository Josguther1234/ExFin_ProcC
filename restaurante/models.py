from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin


class Menu(models.Model):
    nombre =  models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Carta(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)

class CartaInLine(admin.TabularInline):
    model = Carta
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    inlines = (CartaInLine,)

class MenuAdmin(admin.ModelAdmin):
    inlines = (CartaInLine,)
