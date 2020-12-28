from django import forms
#from django.contrib.auth.models import User

from apps.usuario.models import User

class RegisterForm(forms.ModelForm):
	username = forms.CharField(required=True, min_length=4, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-style form-control',
									'id':'username',
									'placeholder': 'Nombre de usuario',
									}))
	email = forms.EmailField(required=True, widget = forms.EmailInput(attrs={
									'class':'form-style form-control',
									'id':'email',
									'placeholder': 'Correo',
									}))
	password = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
									'class':'form-style form-control',
									'id':'password',
									'placeholder': 'Contraseña',
									}))
	password2 = forms.CharField(required=True, widget = forms.PasswordInput(attrs={
									'class':'form-style form-control',
									'id':'password2',
									'placeholder': 'Confirme Contraseña',
									}))
	
	def clean_username(self):
		username = self.cleaned_data.get('username')

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Este usuario ya existe, intente con otro.')

		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo ya existe, intente con otro.')
			
		return email

	def clean(self):
		cleaned_data = super().clean()

		if cleaned_data.get('password2') != cleaned_data.get('password'):
			self.add_error('password', 'La contraseña no coincide')

	def save(self):
		return User.objects.create_user(
			self.cleaned_data.get('username'), 
			self.cleaned_data.get('email'), 
			self.cleaned_data.get('password'),
			)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'password2',
		]

class EditForm(forms.ModelForm):
	first_name = forms.CharField(required=True, min_length=4, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-style form-control',
									'id':'first_name',
									'placeholder': 'Nombre',
									}))
	last_name = forms.CharField(required=True, min_length=4, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-style form-control',
									'id':'last_name',
									'placeholder': 'Apellido',
									}))
	username = forms.CharField(required=True, min_length=4, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-style form-control',
									'id':'username',
									'placeholder': 'Nombre de usuario',
									}))
	email = forms.EmailField(required=True, widget = forms.EmailInput(attrs={
									'class':'form-style form-control',
									'id':'email',
									'placeholder': 'Correo',
									}))
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
		]