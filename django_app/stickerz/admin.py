# coding: utf-8
from __future__ import absolute_import
from django.contrib import admin
from django.utils.translation import ugettext as _
from . import models


class StickerRelation(admin.TabularInline):
    model = models.Sticker
    extra = 0
    # define the sortable
    sortable_field_name = "position"



class StickerContainerAdmin(admin.ModelAdmin):
    inlines = (StickerRelation,)


admin.site.register(models.StickerContainer, StickerContainerAdmin)