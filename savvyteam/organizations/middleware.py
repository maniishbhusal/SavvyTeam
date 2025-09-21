from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Membership


class OrganizationMiddleware:
    """Middleware to enforce organization isolation."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for anonymous users, admin paths, and auth paths
        if (
            not request.user.is_authenticated
            or request.path.startswith("/admin/")
            or request.path.startswith("/accounts/")
        ):
            return self.get_response(request)

        # Skip if on public tenant (schema_name = 'public')
        if (
            hasattr(request, "tenant")
            and request.tenant
            and request.tenant.schema_name == "public"
        ):
            return self.get_response(request)

        # Get current tenant/organization
        if hasattr(request, "tenant") and request.tenant:
            # Check if user has access to this organization
            try:
                membership = get_object_or_404(
                    Membership,
                    user=request.user,
                    organization=request.tenant,
                )
                request.membership = membership
            except Http404:
                # User doesn't have access to this organization
                msg = "You don't have access to this organization"
                raise Http404(msg) from None

        return self.get_response(request)
