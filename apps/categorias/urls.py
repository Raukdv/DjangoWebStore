from django.urls import path, re_path, include

from . import views 

urlpatterns = [
	path('category/add', views.class_add_category.as_view(), name='add_category'),
	path('category/list', views.class_list_category.as_view(), name='list_category'),
	re_path(r'^category/edit/(?P<pk>\d+)/$', views.class_edit_category.as_view(), name='edit_category'),
	re_path(r'^category/delete/(?P<pk>\d+)/$', views.class_delete_category.as_view(), name='delete_category'),
]