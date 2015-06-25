from django.contrib import admin
from . models import Survey
from . models import SurveyUser


class SurveyUserInline(admin.TabularInline):
    model = SurveyUser
    extra = 3


class SurveyAdmin(admin.ModelAdmin):
    inlines = (SurveyUserInline,)

admin.site.register(Survey, SurveyAdmin)
