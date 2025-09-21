from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import OrganizationCreateForm


@login_required
def create_organization(request):
    """View for creating a new organization."""
    if request.method == "POST":
        form = OrganizationCreateForm(request.POST)
        if form.is_valid():
            organization = form.save(user=request.user)
            # Redirect to the new organization's domain
            domain = organization.domains.filter(is_primary=True).first()
            if domain:
                return redirect(f"http://{domain.domain}:8000/")
            return redirect("users:redirect")
    else:
        form = OrganizationCreateForm()

    return render(request, "organizations/create.html", {"form": form})


@login_required
def organization_list(request):
    """View for listing user's organizations."""
    memberships = request.user.memberships.select_related("organization").all()
    return render(request, "organizations/list.html", {"memberships": memberships})
