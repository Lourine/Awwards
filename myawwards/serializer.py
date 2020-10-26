from rest_framework import serializers
from .models import Profile,Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile', 'bio', 'user')

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('name', 'description', 'link', 'date')