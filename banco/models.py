from django.db import models

# Create your models here.
class Banco(models.Model):
	banco = models.CharField('Banco', max_length=100)	
	ag = models.CharField('Agência', max_length=100)	
	cc = models.CharField('C/C', max_length=100)	
	gerente = models.CharField('Gerente', max_length=100)	
	contato = models.CharField('Contato', max_length=100)	
	tel = models.CharField('Telefone', max_length=100)	
	email = models.EmailField('e-mail')
	obs = models.TextField('Observação',null=True, blank=True)

	def __str__(self):
		return self.banco
