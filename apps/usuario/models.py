from django.db import models

from django.contrib.auth.models import User, AbstractUser

#Para sobrescribir el modelo user si es que fuera necesario, se usuara:
#AbstractUser(Posee casi todos los atributos de user) o AbstractBaseUser(Es limitado)

# Create your models here.

class User(AbstractUser):

	def get_full_name(self):
		return '{} {}'.format(self.first_name, self.last_name)

class Customer(User):
	class Meta:
		proxy = True

	def get_products(self):
		return []

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bio = models.TextField()
	