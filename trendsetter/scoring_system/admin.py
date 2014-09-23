from django.contrib import admin
from .models import Account, Transfer


class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('balance', 'created', 'updated')

admin.site.register(Account, AccountAdmin)


class TransferAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('sender', 'receiver', 'amount', 'created', 'updated', 'executed',)
    readonly_fields = ('created', 'updated', 'executed',)

    # disable edit link
    def __init__(self, *args, **kwargs):
        super(TransferAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )


admin.site.register(Transfer, TransferAdmin)
