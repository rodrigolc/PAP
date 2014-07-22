# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.
import widgets.functions as functions

parsers = __import__("widgets.functions")


class Widget(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.CharField(max_length=1000)
    textMessage = models.CharField(max_length=1000)

    # definem se o widget cabe na aba
    preenche_tudo = models.BooleanField()
    altura = models.IntegerField()
    largura = models.IntegerField()
    parser = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Widget'
        verbose_name_plural = 'Widgets'

    def __unicode__(self):
        return "Widget - %s (%s)" % (self.titulo, self.arquivo)

    def parse(self, request, obj):
        return vars(functions)[self.parser](self, request, obj)

# adicionar models especificos, caso necessario
