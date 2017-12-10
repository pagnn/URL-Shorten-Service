from django import forms
from .models import UssURL
from django.core.validators import URLValidator
class SubmitURLForm(forms.ModelForm):
	class Meta:
		model=UssURL
		fields=['url']

	def clean(self):
		cleaned_data=super(SubmitURLForm,self).clean()

	def clean_url(self):
		url=self.cleaned_data['url']
		url_validator=URLValidator()
		try:
			url_validator(url)
		except:
			raise forms.ValidationError('This URL is not Valid.')
		return url