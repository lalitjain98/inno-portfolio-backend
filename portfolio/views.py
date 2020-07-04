from portfolio.models import *
from portfolio.serializers import *

from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework import viewsets

from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_portfolio(request):
    user = CustomUser.objects.first()
    user_serializer = CustomUserSerializer(user, context={'request': request})

    sections = Section.objects.all()
    sections_serializer = SectionSerializer(sections, many=True, context={'request': request})
    
    skills = Skill.objects.all()
    skills_serializer = SkillSerializer(skills, many=True, context={'request': request})

    out = user_serializer.data
    out['sections'] = sections_serializer.data
    out['skills'] = skills_serializer.data
    

    return JsonResponse(out, safe=False)
