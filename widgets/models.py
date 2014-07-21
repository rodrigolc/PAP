# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.


class Widget(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.CharField(max_length=1000)

    # definem se o widget cabe na aba
    preenche_tudo = models.BooleanField()
    tamanho = models.IntegerField()

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'

    def __unicode__(self):
        return "Widget - %s (%s)" % (self.titulo, self.arquivo)



# adicionar models especificos, caso necessario
