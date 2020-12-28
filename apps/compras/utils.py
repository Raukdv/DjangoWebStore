from apps.compras.models import Compra

def get_or_create_cart(request):
	user = request.user if request.user.is_authenticated else None #/Obtener informacion del usuario en cuestion 

	cart_id = request.session.get('cart_id') #None si no se encuentra /obtener el id del carrito
	
	cart = Compra.objects.filter(cart_id=cart_id).first() #[] -> first devuelve None si no cumple con la condicion 
	#/Consultar y traer carrito existente

	if cart is None: #Para cuando no exista un carrito para un ususario anonimo o autenticado
		cart = Compra.objects.create(user=user)

	if user and cart.user is None: #Para cuando exista un usuario autenticado pero no posea carrito
		cart.user = user
		cart.save()

	request.session['cart_id'] = cart.cart_id #se puede usar pk o cart_id #/Creacion de sesion

	return cart

#Crear sesion:
	#request.session['cart_id'] = '1_2/3' #Crear sesion / dic
	#request.session['cart_id'] = None  #Eliminar
	#valor = request.session.get('cart_id') #Consultar
	
	# s = "abcdefghijkl\
	# mnopqrtuvwxy<1234\
	# 56789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# id_len = 6

	# cartid= "".join(random.sample(s, id_len))

	# request.session['cart_id'] = cartid