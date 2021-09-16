from django.urls import path
from softwares.views import (
    SoftwareListView,
    SoftwareDetailView,
    InstallationMethodListView,
    SoftwareInstallationInfoView,
)

urlpatterns = [
    path('', SoftwareListView.as_view(), name='software-list'),
    path('<int:id>/', SoftwareDetailView.as_view(), name='software-detail'),
    path('<int:id>/install/', SoftwareInstallationInfoView.as_view(), name='software-installation-info'),
    path('installation-methods/', InstallationMethodListView.as_view(), name='installation-method-list'),
]
