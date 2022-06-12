from django.db import models
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField

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

class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=True, max_length=500)
    project_image = models.ImageField(blank=False,upload_to='media')
    project_url = models.URLField(blank=False,max_length=255)
    created_on = models.DateField(auto_now_add=True)
    location = LocationField(blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        '''Add new project'''
        self.save()