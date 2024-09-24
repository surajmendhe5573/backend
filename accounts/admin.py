from django.contrib import admin
from .models import RoleMaster

@admin.register(RoleMaster)
class RoleMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'role_description', 'is_active')
