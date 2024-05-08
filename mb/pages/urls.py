from django.urls import path
from .views import HomePageView, ListPageView

urlpatterns =[
    path("", HomePageView.as_view(), name="home"),    
    path("list/", ListPageView.as_view(), name="list"),    
]