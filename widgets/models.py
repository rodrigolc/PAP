from django.db import models

# Create your models here.

class Widget(models.Model):
	titulo = models.CharField(max_length=100)
	arquivo = models.CharField(max_length=1000)
	
	#definem se o widget cabe na aba
	preenche_tudo = models.BooleanField()
	tamanho = models.IntegerField()

	def html(self,args):
	#função que retorna o html do widget
		pass

#adicionar models específicos, caso necessário