from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

# returning fbv sting

def fbv_string(request):
    return HttpResponse('this is fbv sting')

class CBV_string(View):
    def get(self,request):
        return HttpResponse('this us CBV string')

# fbv for returning html page

def fbv_html(request):
    return render(request,'fbv_html.html')

# CBV for returning html page

class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')


# handling form by using fbv

def fbv_form(request):
    return render(request,'fbv_form.html')

# handling form by using CBV

class CBV_form(View):
    def get(self,request):
        return render(request,'CBV_form.html')