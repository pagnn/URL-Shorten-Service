from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import RedirectView,View
from django.contrib import messages

from .models import UssURL
from .forms import SubmitURLForm

from analytics.models import ClickEvent
# Create your views here.


class HomeView(View):
	def get(self,request,*args,**kwargs):
		form=SubmitURLForm()
		context={
			'form':form
		}
		return render(request,'home.html',context)
	def post(self,request,*args,**kwargs):
		form=SubmitURLForm(request.POST)
		template='home.html'
		context={
			'form':form
		}
		if form.is_valid():
			url=form.cleaned_data.get('url')
			obj,created=UssURL.objects.get_or_create(url=url)
		else:
			return render(request,'home.html',context)
		context={
				'form':form,
				'created':created,
				'object':obj,
			}
		return render(request,'shortener/success.html',context)

class UssView(View):
	def get(self,request,shortcode=None,*args,**kwargs):
		obj=get_object_or_404(UssURL,shortcode=shortcode)
		ClickEvent.objects.click_event(obj)
		return HttpResponseRedirect(obj.url)


