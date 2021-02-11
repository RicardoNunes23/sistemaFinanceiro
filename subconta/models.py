from django.db import models

from conta.models import Conta

# Create your models here.

class Subconta(models.Model):
	
	conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
	subconta = models.CharField('Subconta', max_length=100)	

	class Meta:
		ordering =['subconta']
	
	def __str__(self):
		return str(self.subconta) 
