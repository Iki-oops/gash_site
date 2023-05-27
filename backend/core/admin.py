from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    list_display = ('pk', 'username', 'email', 'bio', 'description')
    fieldsets = (
        ('Default_Fields', {'fields': (
            'username',
            'first_name',
            'last_name'
        )}),
        ('Customs_Fields', {'fields': (
            'email',
            'bio',
            'description',
            'avatar',
        )}),
    )
    search_fields = ('username',)
    empty_value_display = '--пусто--'


admin.site.register(CustomUser, UserAdmin)
