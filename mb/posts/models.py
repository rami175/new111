from django.db import models

# Create your models here.
class Post(models.Model):          #inheretance post is a child class of Model
    title = models.CharField(max_length=128)        #composition 
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 