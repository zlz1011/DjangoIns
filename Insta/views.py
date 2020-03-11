#from django.shortcuts import render

# Create your views here.
#当发送request，views.py能调用出来
from django.views.generic import TemplateView

#HelloWorld(是templateview子类) is a TemplateView 
#已经有templateview的attribute/method
class HelloWorld(TemplateView):
    template_name = 'test.html'
    