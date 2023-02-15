from django.db import models


class Rotulo(models.Model):
    codigo_Interno = models.CharField(max_length=200, verbose_name="Codigo Interno")
    n_Cajas = models.CharField(max_length=200, verbose_name="Numero de Cajas")
    Zona_remitente = models.CharField(max_length=200, verbose_name="Zona que Despacha")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "rotulos"
        verbose_name_plural = "rotulos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
