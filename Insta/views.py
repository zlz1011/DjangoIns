#from django.shortcuts import render

# Create your views here.
#当发送request，views.py能调用出来
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.models import Post

#HelloWorld(是templateview子类) is a TemplateView 
#已经有templateview的attribute/method
class HelloWorld(TemplateView):
    template_name = 'test.html'
    
class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'

