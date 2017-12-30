from django import forms

from .validators import validate_url
from .models import UssURL

class SubmitURLForm(forms.ModelForm):
	url=forms.CharField(label='URL',validators=[validate_url])
	class Meta:
		model=UssURL
		fields=['url']