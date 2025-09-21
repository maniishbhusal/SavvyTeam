from django.urls import path

from . import views

app_name = "organizations"

urlpatterns = [
    path("create/", views.create_organization, name="create"),
    path("", views.organization_list, name="list"),
]
