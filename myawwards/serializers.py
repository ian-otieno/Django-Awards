from django.db.models import fields
from rest_framework import serializers
from .models import Project, UserProfile
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'project_title', 'project_image', 'project_description', 'project_link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        user = serializers.SlugRelatedField(
            queryset = User.objects.all(), slug_field='username'
        )
        fields = ['user','profile_photo', 'bio', 'phone_number']
