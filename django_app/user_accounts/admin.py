from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    raw_id_fields = ('invited_by',)
    list_display = ('email', 'full_name', 'preferred_name', 'profile_complete', 'created_at',)
    list_filter = ('profile_complete', 'gender', 'family_status', 'is_staff', 'is_active',)
    search_fields = ('email', 'full_name', 'preferred_name',)

admin.site.register(UserAccount, UserAccountAdmin)

