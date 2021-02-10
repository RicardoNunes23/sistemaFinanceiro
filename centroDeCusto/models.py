from django.db import models

# Create your models here.

class CentroDeCusto(models.Model):
	centroDeCusto = models.CharField('Centro de custo', max_length=100)

	def __str__(self):
		return self.centroDeCusto
