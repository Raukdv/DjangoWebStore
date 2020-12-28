"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from apps.productos.views import class_list_product

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
	path('', class_list_product.as_view(), name='inicio'),
    path('users/', include('apps.usuario.urls')),
    path('pdt/', include('apps.productos.urls')),
    path('ctg/', include('apps.categorias.urls')),
    path('carrito/', include('apps.compras.urls')),
    path('reset/password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html', 
        subject_template_name='registration/password_reset_subject.txt',
        email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('reset/password_done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
