from account.models import CustomUserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

class CustomAdmin(UserAdmin):
    model = CustomUserModel

    fieldsets= UserAdmin.fieldsets + (
        ('Avatar Changing Field', {
            'fields': ['avatar'],
        }),
    )

    list_display=(
        'username', 'email'
    )

admin.site.register(CustomUserModel, CustomAdmin)
    
