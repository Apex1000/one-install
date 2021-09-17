from django.urls import path
from softwares.views import (
    SoftwareListView,
    SoftwareDetailView,
    PackageManagerListView,
    SoftwareInstallationInfoView,
)

urlpatterns = [
    path("", SoftwareListView.as_view(), name="software-list"),
    path("<int:id>/", SoftwareDetailView.as_view(), name="software-detail"),
    path(
        "<int:id>/install/",
        SoftwareInstallationInfoView.as_view(),
        name="software-installation-info",
    ),
    path(
        "package-managers/",
        PackageManagerListView.as_view(),
        name="package-managers-list",
    ),
]
