import random 
import string
from django.conf import settings
# Create your models here.
SHORTCODE_MIN=getattr(settings,'SHORTCODE_MIN',6)
def code_generator(size=SHORTCODE_MIN,chars=string.ascii_lowercase+string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,shortcode=None):
	if shortcode is not None:
		new_code=shortcode
	else:
		new_code=code_generator()
	Klass=instance.__class__
	qs=Klass.objects.filter(shortcode=new_code)
	if qs.exists():
		new_code=code_generator()
		return create_shortcode(instance,new_code)
	return new_code