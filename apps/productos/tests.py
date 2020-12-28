from django.test import TestCase
import json

from apps.productos.models import Producto

# Create your tests here.
class ProductoTest(TestCase):
	def setUp(self):
		Producto.objects.create(title="Camisa", description="Camisa Azul", price=2, available=True, stock=3)
		Producto.objects.create(title="Pantalon", description="Pantalon Negro", price=3, available=False, stock=2)

	def test_product_created_with_a_title(self):
		product = Producto.objects.get(id=1)
		title = 'Camisa'

		self.assertEqual(product.title, title)
