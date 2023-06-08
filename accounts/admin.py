from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "email",
        "username",
        "is_staff",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("backup_email",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("backup_email",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
