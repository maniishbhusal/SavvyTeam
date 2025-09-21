from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Domain
from .models import Membership
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "schema_name", "owner", "created_on")
    list_filter = ("created_on",)
    search_fields = ("name", "schema_name")


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("domain", "tenant", "is_primary")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "joined_at")
    list_filter = ("role", "joined_at")
    search_fields = ("user__email", "organization__name")
