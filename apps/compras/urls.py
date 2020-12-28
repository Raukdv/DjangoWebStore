from django.urls import path, re_path, include

from . import views 

urlpatterns = [
	path('compras', views.cart, name='compras_main'),
	path('compras/agregar', views.add, name='compras_add'),
	path('compras/eliminar', views.remove, name='compras_remove')
]