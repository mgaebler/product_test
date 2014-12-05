# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from models import StaticPage
from django.templatetags.static import static


class StaticPageAdmin(admin.ModelAdmin):
    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('grappelli/tinymce_setup/tinymce_setup.js'),
        ]

admin.site.register(StaticPage, StaticPageAdmin)
