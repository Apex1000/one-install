from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from softwares.models import (
    Software,
    InstallationMethod,
    InstallationInfo
)

from softwares.serializers import (
    SoftwareListSerializer,
    SoftwareDetailSerializer,
    InstallationMethodSerializer,
    InstallationInfoSerializer,
)


# Views

class SoftwareListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SoftwareListSerializer
    queryset = Software.objects.all()


class SoftwareDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SoftwareDetailSerializer
    queryset = Software.objects.all()
    lookup_field = 'id'


class InstallationMethodListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = InstallationMethodSerializer
    queryset = InstallationMethod.objects.all()


class SoftwareInstallationInfoView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = InstallationInfoSerializer
    
    def get_queryset(self):
        software_id = self.kwargs['id']
        queryset = InstallationInfo.objects.filter(software_id=software_id)

        return queryset
