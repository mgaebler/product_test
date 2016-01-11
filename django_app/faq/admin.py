# coding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from django.templatetags.static import static
from .models import FaqGroup, FaqEntry


class FaqEntryRelation(admin.TabularInline):
    model = FaqEntry
    extra = 0
    # define the sortable
    sortable_field_name = "position"


class FaqGroupAdmin(admin.ModelAdmin):
    inlines = (FaqEntryRelation,)

    class Media:
        js = [
            # libs
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            # config
            static('faq/tinymce_setup/tinymce_setup.js'),
        ]

admin.site.register(FaqGroup, FaqGroupAdmin)

# admin.site.register(FaqEntry)
