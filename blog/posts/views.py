from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
# Create your views here.

from django.urls import reverse_lazy
#in order to requier log in 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Status

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
#only showing the draft posts
class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = Post.objects.filter(
            status = draft_status).filter(
                author = self.request.user).order_by("created_on").reverse()
        return context
              
#only shows published posts to everyone
class PublishedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="published")
        context["post_list"] = Post.objects.filter(
            status = draft_status).filter(
                author = self.request.user).order_by("created_on").reverse()
        return context

        
class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    
class PostCreatelView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle", "body", "status"]
    
    def form_valid(self, form):               #override the CreateView method to add new instructions
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title","subtitle", "body", "status"]
    
    #test if the author is the requested user
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")
    
    #test if the author is the requested user
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    


    