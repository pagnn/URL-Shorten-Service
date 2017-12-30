from django.db import models


from shortener.models import UssURL
# Create your models here.

class ClickEventManager(models.Manager):
	def click_event(self,instance):
		if isinstance(instance,UssURL):
			obj,created=self.get_or_create(uss_url=instance)
			obj.count+=1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	uss_url=models.OneToOneField(UssURL)
	count=models.IntegerField(default=0)
	updated=models.DateTimeField(auto_now=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	objects=ClickEventManager()

	def __str__(self):
		return str(self.count)
