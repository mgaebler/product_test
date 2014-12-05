# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin
from django.templatetags.static import static

from .models import ProductTest, Brand, Participation, TestResult


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1


@admin.register(ProductTest)
class ProductTestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at',)
    inlines = (ParticipationInline,)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'brand')
        },),
        ('Images', {
            'fields': (
                ('hero_image', 'hero_image_url',),
                ('list_image', 'list_image_url',),
                ('logo', 'logo_url',),
            )
        }),
        ('Customization', {
            'fields': ('custom_html', 'custom_css',)
        }),
        ('Additional Pages', {
            'fields': ('gallery', 'faq', 'forum', 'test_result')
        }),
        (None, {
            'fields': (
                'published_at',
                'activated_at',
                'ends_at',
                'state',
                ('updated_at', 'created_at',),
            )
        })
    )


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('grappelli/tinymce_setup/tinymce_setup.js'),
        ]


admin.site.register(Brand)