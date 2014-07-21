# -*- coding: utf-8 -*-
from django.db import models

from widgets.models import Widget

# Create your models here.


class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    layout = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __unicode__(self):
        return "Pagina - %s" % (self.titulo)


class Aba(models.Model):
    titulo = models.CharField(max_length=100)
    link = models.CharField(max_length=50)
    pagina = models.ForeignKey(Pagina, related_name='abas')
    widgets = models.ManyToManyField(Widget, related_name='abas')

    class Meta:
        verbose_name = 'Aba'
        verbose_name_plural = 'Abas'

    def __unicode__(self):
        return "Aba - %s" % (self.titulo)

    PROFESSOR = 3
    MONITOR = 2
    ALUNO = 1
    ANONIMO = 0
    TIPOS = [
        (PROFESSOR, "Professor"),
        (MONITOR, "Monitor"),
        (ALUNO, "Aluno"),
        (ANONIMO, "Anonimo")
    ]
    acesso = models.IntegerField(
        max_length=20,
        choices=TIPOS,
        default=ALUNO,
        blank=False
    )
