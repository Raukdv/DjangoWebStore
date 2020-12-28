from django import forms
from apps.categorias.models import Categoria #Modelo de la BD

AVAILABLE_CHOICES =( 
    ("True", "Disponible"), 
    ("False", "No Disponible"),  
) 

class FormCategoria(forms.ModelForm):
	title = forms.CharField(required=True, max_length=50,
								widget = forms.TextInput(attrs={
									'class':'form-control',
									'id':'title',
									'placeholder': 'Titulo de la categoria',
									}))
	description = forms.CharField(required=False, widget = forms.Textarea(attrs={
									'class':'form-control',
									'id':'description',
									'placeholder': 'Descripción de la categoria',
									}))
	products = forms.CheckboxSelectMultiple()
	
	class Meta:
		model = Categoria
		fields = [
			'title',
			'description',
			'products',
		]