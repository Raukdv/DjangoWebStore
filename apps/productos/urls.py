from django.urls import path, re_path, include

from . import views
from django.contrib.auth.decorators import login_required

#app_name = 'productos' <- nombre de la app, para acceder a la ruta en el template sera: productos:nombre_ruta

urlpatterns = [
	path('productos/view', views.data_product_admin, name='admin_view'),
	path('productos/create', views.class_register_product, name='admin_register'),
	path('productos/search', views.class_search_product.as_view(), name='product_search'),
	re_path(r'^adminP/edit/(?P<slug>[\w-]+)/$', views.class_edit_product.as_view(), 
		name='admin_edit'),
	re_path(r'^adminP/delete/(?P<slug>[\w-]+)/$', views.class_delete_product.as_view(), 
		name='admin_delete'),
	re_path(r'^adminP/detail/(?P<slug>[\w-]+)/$', views.class_detail_product.as_view(), 
		name='product_detail'),
] 


#rutas con empresiones regulares#
#ruta para slugs con expresiones regulares:
#re_path(r'^adminP/detail/(?P<slug>[\w-]+)/$', views.class_detail_product.as_view(), name='admin_detail'),

#Sin expresiones regulares:
#path('adminP/detail/<slug:slug>', views.class_detail_product.as_view(), name='admin_detail'),

#Para pks:
#re_path(r'^adminP/edit/(?P<pk>\d+)/$', views.class_edit_product.as_view(), name='admin_edit'),

