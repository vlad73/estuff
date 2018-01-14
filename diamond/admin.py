from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from diamond.models import CustomUser

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('phone','skype','country','city','birthdate',)}),
)

class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS
admin.site.register(CustomUser, MyUserAdmin)

