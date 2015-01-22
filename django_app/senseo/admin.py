# coding: utf-8

from django.contrib import admin
from senseo.models import SEOData
from django.contrib.contenttypes.generic import GenericStackedInline


class SEODataInline(GenericStackedInline):
    model = SEOData
    max_num = 1


class SEODataAdmin(admin.ModelAdmin):
    pass

admin.site.register(SEOData, SEODataAdmin)
