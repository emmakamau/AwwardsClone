from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    prof_pic = models.ImageField(blank=True, upload_to='media')
    bio = models.TextField(blank=True, max_length=255)
    website = models.URLField(blank=True, max_length=50)
    name = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.name

    def save_profile(self):
        '''Add Profile to database'''
        self.save()