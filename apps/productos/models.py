from django.db import models
from django.utils.text import slugify
from django.utils import timezone


import datetime
import uuid

from django.db.models.signals import pre_save

# Create your models here.
class Producto(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField()
    image = models.ImageField(upload_to='productos/', null=False, blank=False)
    available = models.BooleanField()
    stock = models.IntegerField()

    # def save(self, *args, **kwargs):
    # 	self.slug = slugify(self.title)
    # 	self.last_updated = datetime.datetime.now()
    # 	super(Producto, self).save(*args, **kwargs)
    
    def __str__(self):
    	return self.title

def set_slug_and_last_update(sender, instance, *args, **kargs): 
    if instance.title and instance.slug: #Para cuando se actualiza
        slug = slugify(instance.title)

        while Producto.objects.filter(slug=slug).exists():
            slug = slugify( '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] ) ) 

        instance.slug = slug

    elif instance.title and not instance.slug: #Para cuando se crea
        slug = slugify(instance.title)

        while Producto.objects.filter(slug=slug).exists():
            slug = slugify( '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] ) ) 

        instance.slug = slug

  
    instance.last_updated = datetime.datetime.now(tz=timezone.utc)

pre_save.connect(set_slug_and_last_update, sender=Producto) #callback
