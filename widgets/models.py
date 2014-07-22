# -*- coding: utf-8 -*-

from django.db import models
# Create your models here.
import widgets.functions as functions
from usuarios.models import *
parsers = __import__("widgets.functions")


class Widget(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.CharField(max_length=1000)

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


class Nota(models.Model):

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __unicode__(self):
        return "Nota (%s) %s - %s" % (self.aluno.user.username, self.avaliacao.nome, self.nota)
    nota = models.FloatField()
    aluno = models.ForeignKey(Aluno)
    avaliacao = models.ForeignKey("Avaliacao", related_name='notas')


class Avaliacao(models.Model):

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __unicode__(self):
        return "Avaliacao %s - %s %s" % (self.nome, self.peso, self.boletim)
    nome = models.CharField(max_length=100)
    peso = models.FloatField()
    boletim = models.ForeignKey("Boletim", related_name='avaliacoes')


class Boletim(models.Model):

    class Meta:
        verbose_name = 'Boletim'
        verbose_name_plural = 'Boletins'

    def __unicode__(self):
        return "Boletim - %s" % self.nome

    nome = models.CharField(max_length=100)
    widget = models.ForeignKey(Widget)


class TextWidget(models.Model):

    class Meta:
        verbose_name = _('TextWidget')
        verbose_name_plural = _('TextWidgets')

    def __unicode__(self):
        pass
    widget = models.ForeignKey(Widget)
    textMessage = models.CharField(max_length=5120)
