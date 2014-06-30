# -*- coding: utf-8 -*-
from django.db import models

from widgets.models import Widget

# Create your models here.

class Pagina(models.Model):
    titulo = models.CharField(max_length=100)


class Aba(models.Model):
    titulo = models.CharField(max_length=100)
    pagina = models.ForeignKey(Pagina,related_name='abas')
    #permissoes #quem pode acessar a aba.
    widgets = models.ManyToManyField(Widget)