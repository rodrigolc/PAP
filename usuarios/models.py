from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Professor(models.model):
	user = models.OneToOneField(User)

	def get_nome(self):
		#retorna o nome salvo no User
	def get_login(self):
		#idem

class Monitor(models.Model):

	user = models.OneToOneField(User,required=False)
	url_convite = models.CharField(max_length=100)
	cadastrado = models.BooleanField()
	
	def get_nome(self):
		#retorna o nome salvo no User
	def get_login(self):
		#idem


class Aluno(models.Model):

	user = models.OneToOneField(User)	
	
	def get_nome(self):
		#retorna o nome salvo no User
	def get_login(self):
		#idem
