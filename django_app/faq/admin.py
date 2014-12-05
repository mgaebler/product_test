# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import FaqGroup, FaqEntry


class FaqEntryRelation(admin.TabularInline):
    model = FaqEntry
    extra = 0
    # define the sortable
    sortable_field_name = "position"


class FaqGroupAdmin(admin.ModelAdmin):
    inlines = (FaqEntryRelation,)


admin.site.register(FaqGroup, FaqGroupAdmin)

# admin.site.register(FaqEntry)
