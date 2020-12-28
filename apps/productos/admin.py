from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
	fields = ('title', 'description', 'price', 'image', 'available', 'stock')
	list_display = ('__str__', 'slug', 'created_at', 'last_updated')

admin.site.register(Producto, ProductoAdmin)