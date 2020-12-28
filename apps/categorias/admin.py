from django.contrib import admin

# Register your models here.

from .models import Categoria

class CaterogiraAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'created_at')

admin.site.register(Categoria, CaterogiraAdmin)