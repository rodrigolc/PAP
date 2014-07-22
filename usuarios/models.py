# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User Fields
# username
# password
# email
# first_name
# last_name


class TokenConvite(models.Model):
    PROFESSOR = 3
    MONITOR = 2
    ALUNO = 1
    TIPOS = [
        (PROFESSOR, "Professor"),
        (MONITOR, "Monitor"),
        (ALUNO, "Aluno")
    ]
    tipo = models.IntegerField(
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
    # um usuario padrão do Django para cada Usuario da nossa aplicação
    user = models.OneToOneField(User)
    token = models.ForeignKey(TokenConvite)
    pagina = models.ForeignKey("pages.Pagina")

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s - %s" % (self.user.get_username(), self.user.get_full_name())


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
