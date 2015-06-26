from django.contrib import admin
from . models import Survey
from . models import SurveyUser


class SurveyUserInline(admin.TabularInline):
    model = SurveyUser
    extra = 3
    readonly_fields = ('uid', )
    raw_id_fields = ('user', )
    autocomplete_lookup_fields = {
        'fk': ('user', )
    }


class SurveyAdmin(admin.ModelAdmin):
    inlines = (SurveyUserInline,)

admin.site.register(Survey, SurveyAdmin)
