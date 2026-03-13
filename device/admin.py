from django.contrib import admin
from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "last_active_at", "is_blocked")
    search_fields = ("id",)
    list_filter = ("is_blocked",)
