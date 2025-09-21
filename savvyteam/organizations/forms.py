from django import forms
from django.utils.text import slugify

from .models import Domain
from .models import Membership
from .models import Organization


class OrganizationCreateForm(forms.ModelForm):
    """Form for creating a new organization."""

    domain = forms.CharField(
        max_length=100,
        help_text=(
            "This will be your organization's subdomain "
            "(e.g., mycompany.theglowtick.com). "
            "Only letters, numbers, hyphens, and underscores are allowed."
        ),
        required=True,
    )

    class Meta:
        model = Organization
        fields = ["name"]

    def clean_domain(self):
        domain = self.cleaned_data["domain"]
        # Basic domain validation
        if not domain.replace("-", "").replace("_", "").isalnum():
            msg = "Domain can only contain letters, numbers, hyphens, and underscores."
            raise forms.ValidationError(msg)
        return domain.lower()

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.strip():
            msg = "Organization name is required."
            raise forms.ValidationError(msg)
        return name.strip()

    def save(self, commit=True, user=None):  # noqa: FBT002
        organization = super().save(commit=False)
        organization.schema_name = slugify(self.cleaned_data["domain"]).replace(
            "-",
            "_",
        )
        organization.owner = user

        if commit:
            organization.save()

            # Create domain

            domain = Domain(
                domain=self.cleaned_data["domain"],
                tenant=organization,
                is_primary=True,
            )
            domain.save()

            # Create owner membership

            Membership.objects.create(
                user=user,
                organization=organization,
                role=Membership.Role.ADMIN,
            )

        return organization
