from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import RedirectView,View

from .models import UssURL
from .forms import SubmitURLForm
# Create your views here.

class HomeView(View):
	def get(self,request,*args,**kwargs):
		form=SubmitURLForm
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


class UssCBView(RedirectView):
	def get(self,request,shortcode=None,*args,**kwargs):
		return HttpResponse('hello there')
