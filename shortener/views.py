from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import RedirectView,View

from .models import UssURL
from .forms import SubmitURLForm
# Create your views here.

def UssRedirectView(request,shortcode=None):
	print(shortcode)
	obj=get_object_or_404(UssURL,shortcode=shortcode)
	return HttpResponseRedirect(obj.url)

class UssView(View):
	def get(self,request,*args,**kwargs):
		form=SubmitURLForm()
		context={
			'form':form
		}
		return render(request,'shortener/home.html',context)
	def post(self,request,*args,**kwargs):
		form=SubmitURLForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
		context={
			'form':form
		}
		return render(request,'shortener/home.html',context)


