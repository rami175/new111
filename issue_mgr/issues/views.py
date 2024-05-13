from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Issue, Status

#scrum master's view
class IssueListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "issues/list.html"
    model = Issue
    
    def test_func(self):
        return  self.request.user.role == "scrum master"
    

# any team member can view issues (Phase II 1 & 1.1)
class ToDoIssueListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "issues/list.html"
    model = Issue
    #the logged user has a team
    def test_func(self):
        return  self.request.user.team
    
    #show to do issues
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_status = Status.objects.get(name="to do")
        context["issue_list"] = Issue.objects.filter(
            status = issue_status).order_by("created_on").reverse()
        return context
      

# creating a new issue as a product owner (Phase II 2 & 2.1)
class IssueCreatelView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "summary", "description", "status"]
    
    def test_func(self):
        return  self.request.user.role == "product owner"
    
    def form_valid(self, form):              
        form.instance.reporter = self.request.user
        return super().form_valid(form)

#updating an issue as developer(Phase II 3)
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["name","summary", "description", "is_done"]
    
    #test if the user is a developer
    def test_func(self):
        return self.request.user.role == "developer"
    #overriding the form 
    def form_valid(self, form):              
        form.instance.assignee = self.request.user
        return super().form_valid(form)
    
    
    
#updating an issue as scrummaster(Phase II 4 & 4.1)
class ScrumMasterIssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["name","summary", "description", "assignee", "is_done"]
    
    #test if the user is a scrum master
    def test_func(self):
        return self.request.user.role == "scrum master"

   
class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue
