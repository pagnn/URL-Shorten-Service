from django.db import models
from .utils import create_shortcode
from django.conf import settings

SHORTCODE_MAX=getattr(settings,'SHORTCODE_MAX',15)

class UssURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs=super(UssURLManager,self).all(*args,**kwargs)
		qs=qs.filter(active=True)
		return qs

class UssURL(models.Model):
	url = models.CharField(max_length=120)
	shortcode =models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	objects=UssURLManager()

	def save(self,*args,**kwargs):
		self.shortcode=create_shortcode(self)
		super(UssURL,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)
