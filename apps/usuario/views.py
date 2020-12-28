from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import login, authenticate, logout

#from django.contrib.auth.models import User
from apps.usuario.models import User

from .forms import RegisterForm, EditForm

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
# def test_register(request):
# 	form = RegisterForm(request.POST or None)
# 	if request.method == 'POST' and form.is_valid():
# 		username = form.cleaned_data.get('username')
# 		email = form.cleaned_data.get('email')
# 		password = form.cleaned_data.get('password')

# 		user = User.objects.create_user(username, email, password)
# 		if user:
# 			login(request, user)
# 			messages.success(request, 'Usuario creado.')
# 			return redirect('inicio')
# 		else:
# 			messages.error(request, 'Usuario no registrado.')
# 			return redirect('register')

# 	return render(request, 'registration/create_user.html', {'form': form})

#Vista de todos los usuarios solo para admins
def data_user(request):
	if request.user.is_superuser == True and request.user.is_authenticated:
		current_user = request.user
		usern = User.objects.all().order_by('id')
		return render(request, 'main_views/admin_view.html', 
			{
			'current_user':current_user,
			'usern':usern,
			'message':'Edición de usuarios',
			'title':'Usuarios',
			})
	if request.user.is_authenticated:
		current_user = request.user
		return render(request, 'main_views/user_view.html', 
			{
			'current_user':current_user,
			'message':'Edición de usuario',
			'title':'Usuario',
			})
	else:
		return render(request, 'main_views/user_view.html', 
			{
			'current_user':{},
			'message':'Acceso denegado',
			'title':'Denegado',
			})

#Vista de loggeo
def class_login(request):
	if request.user.is_authenticated:
		return redirect('inicio')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('inicio')
		else:
			messages.error(request, 'Usuario o contraseña no validos')
			return redirect('login')
	else:
		return render(request, 'register/login.html')

#vista de registro y login
def class_register(request):
	if request.user.is_authenticated:
		return redirect('inicio')

	form = RegisterForm(request.POST or None)
		
	if request.method == 'POST' and form.is_valid():
		user = form.save()
		if user:
			login(request, user)
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('inicio')
		else:
			messages.error(request, 'Usuario no registrado.')
			return redirect('register')
	else:
		return render(request, 'register/create_user.html', {'form':form})

#vista de edicion
class class_edit(SuccessMessageMixin, UpdateView):
	model = User
	form_class = EditForm
	template_name = 'register/edit_user.html'
	
	def get_context_data(self, **kwargs):
		context = super(class_edit, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		persona = self.model.objects.get(id=pk)
		if 'form' not in context:
			context['form'] = self.form_class()
		context['id'] = pk
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_persona = kwargs['pk']
		persona = self.model.objects.get(id=id_persona)

		form = self.form_class(request.POST, instance=persona)
		if form.is_valid():
			form.save()
			messages.success(request, 'Usuario actualizado')
			return redirect('test')
		else:
			return self.render_to_response(self.get_context_data(form=form))

#vista de eliminacion
class class_delete(SuccessMessageMixin, DeleteView):
	model = User 
	template_name = 'register/delete_data.html'
	success_url = reverse_lazy('test')
	context_object_name = 'user' #esta devolviendo una instancia de object y otra de user.
	
#funciona de deslogeo
def logout_view(request):
	logout(request)
	messages.info(request, 'Sesion finalizada.')
	return redirect('login')


