from django.contrib import admin
from .models import Password, Service


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    fields = [
        "service_name",
        "encrypted_password",
    ]
    search_fields = [
        "service_name",
    ]
    readonly_fields = ['encrypted_password']


@admin.register(Service)
class ServcieAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at", "id")
