from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreateForm
from django.contrib.auth import get_user_model
from .models import User


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ("national_code", "name", "family")
    list_filter = ("is_admin",)
    readonly_fields = ("last_login",)
    fieldsets = (
        ('Main', {'fields': ('national_code', "name", "family")}),
        (
            'Permissions',
            {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {'fields': ('national_code', 'name', 'family')})
    )
    search_fields = ('national_code',)
    ordering=('name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
