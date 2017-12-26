from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from .utils import create_shortcode
SHORTCODE_MAX=getattr(settings,'SHORTCODE_MAX',15)

class UssURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs=super(UssURLManager,self).all(*args,**kwargs)
		qs=qs.filter(active=True)
		return qs
	def refresh_shortcodes(self,items=None):
		qs=UssURL.objects.filter(id__gte=0)
		if items and isinstance(items,int):
			qs=qs.order_by('-timestamp')[:items]
		count=0
		for q in qs:
			q.shortcode=create_shortcode(q)
			count+=1
		return str(count)
class UssURL(models.Model):
	url = models.CharField(max_length=120)
	shortcode =models.CharField(max_length=SHORTCODE_MAX,unique=True,null=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	active=models.BooleanField(default=True)

	objects=UssURLManager()

	def __str__(self):
		return str(self.url)

def pre_save_uss_receiver(sender,instance,*args,**kwargs):
	if not instance.shortcode:
		instance.shortcode=create_shortcode(instance)
pre_save.connect(pre_save_uss_receiver,sender=UssURL)