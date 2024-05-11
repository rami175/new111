from django.urls import path 
from posts import views

urlpatterns =[
    path("", views.PostListView.as_view(), name="list"),
    path("drafts/", views.DraftPostListView.as_view(), name="drafts"),
    path("published/", views.PublishedPostListView.as_view(), name="published"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.PostCreatelView.as_view(), name="new"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
        
]