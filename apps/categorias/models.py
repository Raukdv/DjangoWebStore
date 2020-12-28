from django.db import models

from apps.productos.models import Producto

# Create your models here.
class Categoria(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	products = models.ManyToManyField(Producto, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title