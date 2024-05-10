from django.shortcuts import render

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    
)

from .models import Post


# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    
class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
   