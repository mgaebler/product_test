from django.contrib import admin
from .models import FaqGroup, FaqEntry


class FaqEntryRelation(admin.TabularInline):
    model = FaqEntry
    extra = 1


class FaqGroupAdmin(admin.ModelAdmin):
    inlines = (FaqEntryRelation,)


admin.site.register(FaqGroup, FaqGroupAdmin)

# admin.site.register(FaqEntry)
