from rest_framework import serializers
from .models import Project, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','prof_pic','bio',
                  'website','name','bio','phone','fax_number',
                  'linkedin')