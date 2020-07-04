from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_number = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    
    linkedin_url = models.URLField(max_length=200, null=True)
    github_url = models.URLField(max_length=200, null=True)

    designation = models.CharField(max_length=200, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)

class Section(models.Model):
    title = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.title

class Experience(models.Model):
    
    title = models.CharField(max_length=100, null=False)
    subtitle = models.CharField(max_length=100, null=False, blank=True)
    
    start_date = models.DateField(auto_now_add=False, null=True, blank=True)

    is_present = models.BooleanField(default=False)
    
    has_definite_start_date = models.BooleanField(default=True)

    end_date = models.DateField(auto_now_add=False, null=True)

    description = models.TextField(null=True, blank=True)

    section = models.ForeignKey(to=Section, related_name='experiences', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' + self.subtitle

class Skill(models.Model):
    title = models.CharField(max_length=100, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title
