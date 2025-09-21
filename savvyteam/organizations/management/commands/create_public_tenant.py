import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from savvyteam.organizations.models import Domain
from savvyteam.organizations.models import Organization

User = get_user_model()


class Command(BaseCommand):
    help = "Create the public tenant for the main website"

    def handle(self, *args, **options):
        # Create or get a superuser for the public tenant
        try:
            admin_user = User.objects.get(email="admin@example.com")
        except User.DoesNotExist:
            admin_password = os.getenv("PUBLIC_TENANT_ADMIN_PASSWORD", "admin123")
            admin_user = User.objects.create_superuser(
                email="admin@example.com",
                password=admin_password,
                name="Admin User",
            )
            self.stdout.write(
                self.style.SUCCESS(f"Created admin user: {admin_user.email}"),
            )

        # Create public tenant
        try:
            public_tenant = Organization.objects.get(schema_name="public")
            self.stdout.write(
                self.style.WARNING("Public tenant already exists"),
            )
        except Organization.DoesNotExist:
            public_tenant = Organization(
                schema_name="public",
                name="SavvyTeam Main",
                owner=admin_user,
            )
            public_tenant.save()

            # Create domains for public tenant useful in local dev
            # Note: Do not override if a domain already exists for a different tenant.
            for host, is_primary in (("127.0.0.1", True), ("localhost", False)):
                Domain.objects.get_or_create(
                    domain=host,
                    defaults={"tenant": public_tenant, "is_primary": is_primary},
                )

            self.stdout.write(
                self.style.SUCCESS(f"Created public tenant: {public_tenant.name}"),
            )
