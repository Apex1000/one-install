from rest_framework import serializers

from softwares.models import Software, PackageManager, InstallationInfo


class PackageManagerSerializer(serializers.ModelSerializer):
    os = serializers.SerializerMethodField()

    class Meta:
        model = PackageManager
        fields = (
            "id",
            "name",
        )

    def get_os(self, obj):
        return obj.operating_system.name if obj.operating_system else None


class InstallationInfoSerializer(serializers.ModelSerializer):
    software = serializers.SerializerMethodField()
    platform = serializers.SerializerMethodField()
    extension = serializers.SerializerMethodField()
    script = serializers.SerializerMethodField()

    class Meta:
        model = InstallationInfo
        fields = (
            "software",
            "package_name",
            "download_url",
            "platform",
            "extension",
            "script",
        )

    def get_software(self, obj):
        return obj.software.name if obj.software else None

    def get_platform(self, obj):
        return obj.method.operating_system.name if obj.method else None

    def get_extension(self, obj):
        return obj.method.package_manager if obj.method else None

    def get_script(self, obj):
        return obj.script if obj.script else None


class SoftwareListSerializer(serializers.ModelSerializer):
    os = serializers.SerializerMethodField()

    class Meta:
        model = Software
        fields = ("id", "name", "os")

    def get_os(self, obj):
        return [os.name for os in obj.os.all()]


class SoftwareDetailSerializer(serializers.ModelSerializer):
    installation_methods = serializers.SerializerMethodField()
    install = serializers.SerializerMethodField()
    os = serializers.SerializerMethodField()

    class Meta:
        model = Software
        fields = (
            "id",
            "name",
            "os",
            "installation_methods",
            "install",
        )

    def get_os(self, obj):
        return [os.name for os in obj.os.all()]

    def get_installation_methods(self, obj):
        return InstallationInfo.objects.filter(software=obj).values_list(
            "method__package_manager", flat=True
        )

    def get_install(self, obj):
        return InstallationInfoSerializer(
            PackageManager.objects.filter(software=obj), many=True
        ).data
