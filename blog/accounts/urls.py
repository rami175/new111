from django.urls import path
from .views import SighnView

urlpatterns = [
    path('', SighnView.as_view(), name='signup'),
    
]