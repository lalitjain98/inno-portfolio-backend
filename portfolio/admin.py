from django.contrib import admin

# Register your models here.

from portfolio.models import *

admin.site.register(CustomUser)
admin.site.register(Section)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Feedback)
