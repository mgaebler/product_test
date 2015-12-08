from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    raw_id_fields = ('invited_by',)
    list_display = ('email', 'full_name', 'preferred_name', 'profile_complete',)
    search_fields = ('email', 'full_name', 'preferred_name', 'profile_complete',)

admin.site.register(UserAccount, UserAccountAdmin)

