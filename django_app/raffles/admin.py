# coding: utf-8
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from raffles.models import Raffle
from senseo.admin import SEODataInline
from simple_comments.models import Comment


class CommentInline(GenericStackedInline):
    model = Comment
    raw_id_fields = ('creator', )
    autocomplete_lookup_fields = {
        'fk': ('creator', )
    }


@admin.register(Raffle)
class RaffleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Images'), {'classes': ('collapse',), 'fields': ('logo', 'list_image')}),
        (_('Dates'), {'classes': ('collapse',), 'fields': ('starts_at', 'ends_at')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', )}),
    )

    inlines = (CommentInline, SEODataInline)
    list_display = ('url', 'title', "starts_at", "ends_at")
    list_filter = ('enable_comments', "starts_at", "ends_at")
    search_fields = ('url', 'title', 'content')

    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('raffles/tinymce_setup/tinymce_setup.js'),
        ]
