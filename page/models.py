from django.db import models

#import widgets.models.Widget

# Create your models here.

class Pagina(models.Model):
	titulo = models.CharField(max_length=100)
	#abas = lista de abas
	#layout = template do layout

	def adicionar_aba(self,aba):
		#self.abas.push(aba)
		#resto do codigo para adicionar aba
		pass

	def remover_aba(self,aba):
		#if aba in self.abas:
		#	del self.abas.find(aba)
		#resto
		pass

	def reordenar_abas(self,aba,pos):
		#blabla stub
		pass

	def mudar_layout(self,layout):
		self.layout = layout


class Aba(models.Model):
	titulo = models.CharField(max_length=100)

	#widgets = lista de widgets

	def adicionar_widget(self,widget):
		#blabla stub
		pass

	def remover_widget(self,widget):
		#blablalba
		pass

	def mover_widget(self,widget,pos):
		#blabla
		pass

