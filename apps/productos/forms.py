from django import forms
from apps.productos.models import Producto #Modelo de la BD

AVAILABLE_CHOICES =( 
    ("True", "Disponible"), 
    ("False", "No Disponible"),  
) 

class EditFormProduct(forms.ModelForm):
	title = forms.CharField(required=True, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-control',
									'id':'title',
									'placeholder': 'Titulo del producto',
									}))
	description = forms.CharField(required=True, widget = forms.Textarea(attrs={
									'class':'form-control',
									'id':'description',
									'placeholder': 'Descripción del producto',
									}))
	price = forms.DecimalField(required=True, max_digits=10, decimal_places=3,
								widget = forms.NumberInput(attrs={
									'class':'form-control',
									'id':'price',
									'placeholder': 'Precio del producto',
									}))
	image = forms.ImageField(widget = forms.ClearableFileInput(attrs={
									'id':'image',
									}))

	available = forms.ChoiceField(required=False, choices=AVAILABLE_CHOICES,
								widget = forms.Select(attrs={
									'class':'form-control select',
									'id':'available',
									}))
	stock = forms.IntegerField(required=False, widget = forms. NumberInput(attrs={
									'class':'form-control',
									'id':'stock',
									'placeholder':'Cantidad en stock'
									}))
	
	class Meta:
		model = Producto
		fields = [
			'title',
			'description',
			'price',
			'image',
			'available',
			'stock',
		]

class RegisterFormProduct(forms.ModelForm):
	title = forms.CharField(required=True, max_length=50,
								widget = forms.Textarea(attrs={
									'class':'form-control',
									'id':'title',
									'placeholder': 'Titulo del producto',
									}))
	description = forms.CharField(required=True, widget = forms.Textarea(attrs={
									'class':'form-control',
									'id':'description',
									'placeholder': 'Descripción del producto',
									}))
	price = forms.DecimalField(required=True, max_digits=10, decimal_places=3, 
								widget = forms.NumberInput(attrs={
									'class':'form-control',
									'id':'price',
									'placeholder': 'Precio del producto',
									}))
	image = forms.ImageField(widget = forms.ClearableFileInput(attrs={
									'id':'image',
									}))
	available = forms.ChoiceField(required=False, choices=AVAILABLE_CHOICES,
								widget = forms.Select(attrs={
									'class':'form-control select',
									'id':'available',
									}))
	stock = forms.IntegerField(required=False, widget = forms. NumberInput(attrs={
									'class':'form-control',
									'id':'stock',
									'placeholder':'Cantidad en stock'
									}))
	
	def clean_title(self):
		title = self.cleaned_data.get('title')

		if Producto.objects.filter(title=title).exists():
			raise forms.ValidationError('Este titulo ya existe, intente con otro.')

		return title

	class Meta:
		model = Producto
		fields = [
			'title',
			'description',
			'price',
			'image',
			'available',
			'stock',
		]