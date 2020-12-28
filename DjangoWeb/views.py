# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect

# from django.contrib import messages
# from django.urls import reverse_lazy

# from django.views.generic.list import ListView

# from django.contrib.messages.views import SuccessMessageMixin

# from django.contrib.auth.models import User
# from apps.productos.models import Producto

# def index(request):

# 	products = Producto.objects.all().order_by('-id')
# 	return render(request, 'inicio/index.html', 
# 		{
# 		'message':'Listado De Productos', 
# 		'title':'Productos',
# 		'products':products,
# 		})

#Vista de administrador o de usuario, se puede cambiar por el siguiente class view de ListView
# def data_user(request):
# 	if request.user.is_superuser == True and request.user.is_authenticated:
# 		current_user = request.user
# 		usern = User.objects.all().order_by('id')
# 		return render(request, 'main_views/admin_view.html', 
# 			{
# 			'current_user':current_user,
# 			'usern':usern,
# 			'message':'Pruebas con usuarios',
# 			'title':'Pruebas',
# 			})
# 	if request.user.is_authenticated:
# 		current_user = request.user
# 		return render(request, 'main_views/user_view.html', 
# 			{
# 			'current_user':current_user,
# 			'message':'Pruebas con usuarios',
# 			'title':'Pruebas',
# 			})
# 	else:
# 		return render(request, 'main_views/user_view.html', 
# 			{
# 			'current_user':{},
# 			'message':'Pruebas con usuarios:',
# 			'title':'Pruebas',
# 			})

# Vista class view: ----------------------------------------------------------------------------
# class data_user(SuccessMessageMixin, ListView):	
# 	def get(self, request, *args, **kwargs):
# 		if request.user.is_superuser == True and request.user.is_authenticated:
# 			current_user = request.user
# 			usern = User.objects.order_by('id')
# 			return render(request, 'main_views/admin_view.html', 
# 				{
# 				'current_user':current_user,
# 				'usern':usern,
# 				'message':'Pruebas con usuarios',
# 				'title':'Pruebas',
# 				})
# 		if request.user.is_authenticated:
# 			current_user = request.user
# 			return render(request, 'main_views/user_view.html', 
# 				{
# 				'current_user':current_user,
# 				'message':'Pruebas con usuarios',
# 				'title':'Pruebas',
# 				})
# 		else:
# 			return render(request, 'main_views/user_view.html', 
# 				{
# 				'current_user':{},
# 				'message':'Pruebas con usuarios:',
# 				'title':'Pruebas',
# 				})
# -----------------------------------------------------------------------------------------------