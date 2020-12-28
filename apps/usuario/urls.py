from django.contrib import admin
from django.urls import path, include, re_path

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('accounts/login', views.class_login, name='login'),
	path('accounts/create', views.class_register, name='register'),
	path('accounts/logout', views.logout_view, name='logout'),
	path('accounts/check/', views.data_user, name='test'),
	re_path(r'^edit/(?P<pk>\d+)/$', views.class_edit.as_view(),  name='edit'),
	re_path(r'^delete/(?P<pk>\d+)/$', views.class_delete.as_view(),  name='delete'),
	
] 



