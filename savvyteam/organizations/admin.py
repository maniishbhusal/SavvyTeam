from django.contrib import admin

from .models import Domain
from .models import Membership
from .models import Organization


class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_header = "Tenant Manager Admin"
        self.index_title = "Welcome to Tenant Manager Admin"
        self.register(Organization)
        self.register(Domain)
        self.register(Membership)


tenant_admin_site = TenantAdminSite(name="tenant_admin_site")
