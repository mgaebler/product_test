# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
from django.contrib import admin
from .models import Account, Transfer


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('balance', 'created', 'updated')
    list_display = ("name", "balance")
    search_fields = ("name", "customer__email")
admin.site.register(Account, AccountAdmin)


class TransferAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('sender', 'receiver', 'amount', 'reference', 'created', 'updated', 'executed')
    readonly_fields = ('created', 'updated', 'executed',)
    search_fields = ("sender__name", "sender__customer__email", "receiver__name", "receiver__customer__email")
    raw_id_fields = ('sender', 'receiver',)
    autocomplete_lookup_fields = {
        'fk': ['sender', 'receiver']
    }

    # disable edit link
    def __init__(self, *args, **kwargs):
        super(TransferAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )
admin.site.register(Transfer, TransferAdmin)
