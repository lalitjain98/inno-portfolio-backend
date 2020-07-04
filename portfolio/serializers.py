from rest_framework import serializers
from portfolio.models import *

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):

    # experiences = ExperienceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Section
        fields = ['id', 'title', 'experiences']
        depth = 1

class CustomUserSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = CustomUser
        fields = ['user', 'mobile_number', 'location', 'linkedin_url', 'github_url', 'designation']
