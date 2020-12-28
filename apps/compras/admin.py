from django.contrib import admin
from django.contrib.admin.sites import site

from .models import Compra, CompraCantidades
# Register your models here.

@admin.register(Compra, CompraCantidades, site=site)
class CompraAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at')

#admin.site.register(Compra, CompraAdmin)