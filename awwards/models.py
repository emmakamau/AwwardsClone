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

    @classmethod
    def delete_project(cls,id):
        ''' Delete project from database '''
        project = Project.objects.get(id=id)
        project.delete()

    @property
    def saved_likes(self):
        return self.likes.count()

class Comment(models.Model):
    user_profile = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    user_comment = models.CharField(blank=False, max_length=255)
    project_associated = models.ForeignKey(Project,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user_comment

    def save_comment(self):
        '''Add Comment to database'''
        self.save()

    @classmethod
    def delete_comment(cls,id):
        ''' Delete comment from database '''
        comment = Comment.objects.get(id=id)
        comment.delete()

class PostVote(models.Model):
    profile_vote = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    post_voted = models.ForeignKey(Project,null=True,on_delete=models.SET_NULL,related_name='likes')

    def save_like(self):
        self.save()