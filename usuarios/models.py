# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TokenConvite(models.Model):
    PROFESSOR = "PR"
    MONITOR = "MO"
    ALUNO = "AL"
    TIPOS = [
        (PROFESSOR, "Professor"),
        (MONITOR, "Monitor"),
        (ALUNO, "Aluno")
    ]
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        default=ALUNO,
        blank=False
    )
    token = models.CharField(max_length=20, primary_key=True)
    usado = models.BooleanField(default=False)

    def __unicode__(self):
        return "TokenConvite - %s (%s)" % (self.token, self.get_tipo_display())



class Usuario(models.Model):
    #um usuario padrão do Django para cada Usuario da nossa aplicação
    user = models.OneToOneField(User)
    token = models.ForeignKey(TokenConvite)

    class Meta:
        abstract = True

    def __unicode__(self):
        pass


class Professor(Usuario):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'


class Monitor(Usuario):
    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'


class Aluno(Usuario):
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
