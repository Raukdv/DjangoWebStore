from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404

from apps.compras.models import Compra
from apps.productos.models import Producto
from apps.compras.utils import get_or_create_cart

# Create your views here.
def cart(request):
	
	cart = get_or_create_cart(request)

	return render(request, 'carts/carts_main_view.html', {
		'cart':cart
		})

def add(request):
	cart = get_or_create_cart(request)

	if request.method == 'POST':
		idproduct = request.POST.get('product_id')

		product = get_object_or_404(Producto ,pk=idproduct)

		cart.products.add(product)
		messages.success(request, 'El Producto fue agregado.')
		return render(request, 'carts/carts_add_view.html', {
			'producto':product
			})

	else:

		messages.warning(request, 'El Producto no pudo ser agregado.')
		return redirect('product_detail')

def remove(request):
	cart = get_or_create_cart(request)

	idproduct = request.POST.get('product_id')

	product = get_object_or_404(Producto ,pk=idproduct)

	cart.products.remove(product)

	messages.success(request, 'El Producto: {}, fue eliminado.'.format(product.title))
	return redirect('compras_main')