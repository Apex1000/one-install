from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from softwares.models import Software, PackageManager, InstallationInfo

from softwares.serializers import (
    SoftwareListSerializer,
    SoftwareDetailSerializer,
    PackageManagerSerializer,
    InstallationInfoSerializer,
)


# Views


class SoftwareListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SoftwareListSerializer

    def get_queryset(self):
        queryset = Software.objects.all()

        name = self.request.query_params.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class SoftwareDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SoftwareDetailSerializer
    queryset = Software.objects.all()
    lookup_field = "id"


class PackageManagerListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PackageManagerSerializer
    queryset = PackageManager.objects.all()


class SoftwareInstallationInfoView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = InstallationInfoSerializer

    def get_queryset(self):
        software_id = self.kwargs["id"]
        queryset = InstallationInfo.objects.filter(software_id=software_id)

        return queryset
