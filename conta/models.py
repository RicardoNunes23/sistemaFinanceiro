from django.db import models

# Create your models here.

class Conta(models.Model):
	conta = models.CharField('Conta', max_length=100, unique=True)	

	def __str__(self):
		return self.conta