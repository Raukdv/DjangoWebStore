from django.db import models

from apps.usuario.models import User
from apps.productos.models import Producto

from django.db.models.signals import pre_save, m2m_changed

import uuid

import decimal

# Create your models here.

class Compra(models.Model):
	cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #Uno a mucho
	products = models.ManyToManyField(Producto, through='CompraCantidades') #Muchos a Muchos
	subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
	total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)

	#Comision del total
	#IVA = 16% = 0.16

	IVA = 0.16

	def __str__(self):
		return self.cart_id

	#Para actualizar los subtotales y totales

	def update_totals(self): #Callback entero
		self.update_subtotal()
		self.update_total()

	def update_subtotal(self): #Accion para subtotales
		self.subtotal = sum([ producto.price for producto in self.products.all() ])
		self.save()

	def update_total(self): #Accion para totales
		self.total = self.subtotal + (self.subtotal * decimal.Decimal(Compra.IVA))
		self.save()

class CompraCantidades(models.Model):
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)

#Callbacks que se ejecutan

def set_cart_id(sender, instance, *args, **kwargs):
	if not instance.cart_id:
		instance.cart_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
	if action in ['post_add',  'post_remove',  'post_clear']:
		instance.update_totals()

#Registro de callback 
pre_save.connect(set_cart_id, sender=Compra)
m2m_changed.connect(update_totals, sender=Compra.products.through)