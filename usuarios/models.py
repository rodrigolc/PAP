from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Professor(models.Model):
	user = models.OneToOneField(User)

	def get_nome(self):
		#retorna o nome salvo no User
		pass

	def get_login(self):
		#idem
		pass

class Monitor(models.Model):

	user = models.OneToOneField(User)
	url_convite = models.CharField(max_length=100)
	cadastrado = models.BooleanField()
	
	def get_nome(self):
		#retorna o nome salvo no User
		pass

	def get_login(self):
		#idem
		pass



class Aluno(models.Model):

	user = models.OneToOneField(User)	
	
	def get_nome(self):
		#retorna o nome salvo no User
		pass

	def get_login(self):
		#idem
		pass

