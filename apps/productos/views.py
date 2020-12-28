from django.shortcuts import render, redirect

from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import EditFormProduct, RegisterFormProduct

from apps.productos.models import Producto

from django.db.models import Q



#Vista con requisitos de administrador:
def data_product_admin(request):
	if request.user.is_superuser == True and request.user.is_authenticated:
		current_user = request.user
		productd = Producto.objects.all().order_by('-id')
		return render(request, 'products_views/main_view_product.html', 
			{
			'current_user':current_user,
			'productd':productd,
			'message':'Bienvenido: {}'.format(current_user.username),
			'title':'Edición',
			})
	else:
		return render(request, 'products_views/main_view_product.html',
			{
			'message':'Usted no posee permisos de administrador:',
			'title':'Sin Permisos',
			})

#Vista de registro o creación:
def class_register_product(request):
	if request.user.is_superuser == False:
		return redirect('inicio')

	form = RegisterFormProduct(request.POST or None, request.FILES or None)	
	if request.user.is_superuser == True and request.user.is_authenticated and request.method == 'POST' and form.is_valid():
		productoc = form.save()
		if productoc:
			messages.success(request, 'El Producto: {}, fue creado.'.format(productoc.title))
			return redirect('admin_view')
		else:
			messages.error(request, 'Producto no registrado.')
			return redirect('admin_register') #Revisar caul era la view de aqui
	else:
		return render(request, 'products_views/create_view_product.html', {
			'form':form
			})

#Vista de listado:
class class_list_product(ListView):
	template_name = 'inicio/index.html'
	queryset = Producto.objects.all().order_by('-id')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['message'] = 'Listado de productos'
		context['products'] = context['producto_list'] #se puede usar object_list o producto_list sin tener que definir una nueva llave en context
		return context

#vista de busqueda:
class class_search_product(ListView):
	template_name = 'products_views/search.html'

	def get_queryset(self):
		#__icontains: SELECT * FROM Producto WHERE title like 'valor' la i solo indica que no es sensible a "M" o "m"
		filters = Q(title__icontains=self.query()) | Q(categoria__title__icontains=self.query())
		return Producto.objects.filter(filters) 

	def query(self):
		return self.request.GET.get('q')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['query'] = self.query()
		context['products'] = context['producto_list'] #Importante ya que se esta reusando los snippets de index  productv y "searchs" para mostrar
		context['count'] = context['producto_list'].count()
		return context

#vista detallada de productos:
class class_detail_product(DetailView):
	model = Producto
	template_name = 'products_views/detail_view_product.html'
	#context_object_name = 'p' <sobrescribe el nombre del objeto del contexto>

#Vista de edición:
class class_edit_product(SuccessMessageMixin, UpdateView):
	model = Producto
	form_class = EditFormProduct
	template_name = 'products_views/edit_view_product.html'
	
	def get_context_data(self, **kwargs):
		context = super(class_edit_product, self).get_context_data(**kwargs)
		slug = self.kwargs.get('slug', '')
		#producto = self.model.objects.get(id=pk)
		if 'form' not in context:
			context['form'] = self.form_class()
		context['slug'] = slug
		#print(context)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		slug_producto = kwargs['slug']
		producto = self.model.objects.get(slug=slug_producto)

		form = self.form_class(request.POST, request.FILES, instance=producto)
		if form.is_valid():
			form.save()
			messages.success(request, 'Producto actualizado')
			return redirect('admin_view')
		else:
			messages.error(request, 'Producto no actualizado.')
			return self.render_to_response(self.get_context_data(form=form))

#Vista de eliminación:
class class_delete_product(SuccessMessageMixin, DeleteView):
	model = Producto
	template_name = 'products_views/delete_view_product.html'
	success_url = reverse_lazy('admin_view')
