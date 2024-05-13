from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=128)
    describtion = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    
    
class Team(models.Model):
    name = models.CharField(max_length=128)
    describtion = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role= models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    
    
# class Status(models.Model):
#      name = models.CharField(max_length=128)
#      describtion = models.CharField(max_length=256)
    
#      def __str__(self):
#         return self.name