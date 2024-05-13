from django.urls import path 
from issues import views

urlpatterns =[
    path("list/", views.ToDoIssueListView.as_view(), name="to_do"),
    path("list/", views.IssueListView.as_view(), name="list"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("new/", views.IssueCreatelView.as_view(), name="new"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("<int:pk>/full_edit/", views.ScrumMasterIssueUpdateView.as_view(), name="full_edit"),
]