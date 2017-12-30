from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
def validate_url(value):
	url_validator=URLValidator()
	reg_value=None
	if 'http' in value:
		reg_value=value
	else:
		reg_value='http://'+value
	try:
		url_validator(reg_value)
	except:
		raise ValidationError('This URL is not valid.')
	return reg_value
