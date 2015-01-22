from django.contrib import admin
from static_pages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static
from static_pages.forms import FlatpageForm
from senseo.admin import SEODataInline

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    inlines = (SEODataInline,)
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

    class Media:
        js = [
            static('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'),
            static('static_pages/tinymce_setup/tinymce_setup.js'),
        ]

admin.site.register(FlatPage, FlatPageAdmin)
