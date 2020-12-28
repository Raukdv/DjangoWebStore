from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from apps.categorias.models import Categoria

from .forms import FormCategoria

# Create your views here.
class class_add_category(CreateView):
	model = Categoria
	form_class = FormCategoria
	template_name = 'main/categories_create_view.html'
	success_url = reverse_lazy('inicio')

class class_list_category(ListView):
	template_name = 'main/categories_list_view.html'
	queryset = Categoria.objects.all().order_by('-id') #model = Categoria

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Categorias'
		context['categorias'] = context['categoria_list'] #Instancias posibles: object_list o categortia_list
		return context

class class_edit_category(SuccessMessageMixin, UpdateView):
	model = Categoria
	form_class = FormCategoria
	template_name = 'main/categories_create_view.html'
	
	def get_context_data(self, **kwargs):
		context = super(class_edit_category, self).get_context_data(**kwargs)
		#pk = self.kwargs.get('pk', 0)
		if 'form' not in context:
			context['form'] = self.form_class()
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_category = kwargs['pk'] #self.kwargs.get('pk', 0) // recive la palabra clave del POST: ej; pk o slug
		categoria = self.model.objects.get(id=id_category)

		form = self.form_class(request.POST, instance=categoria)
		if form.is_valid():
			form.save()
			messages.success(request, 'La Categoria: {}, fue actualizada'.format(categoria.title))
			return redirect('list_category')
		else:
			messages.error(request, 'Producto no actualizado.')
			return self.render_to_response(self.get_context_data(form=form))

class class_delete_category(SuccessMessageMixin, DeleteView):
	model = Categoria
	template_name = 'main/categories_delete_view.html'
	success_url = reverse_lazy('admin_view')