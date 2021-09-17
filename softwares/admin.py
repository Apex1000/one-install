from django.contrib import admin
from softwares.models import (
    OperatingSystem,
    PackageManager,
    Software,
    InstallationInfo,
)

# Register your models here.


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_filter = ("os",)


class InstallationInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "software", "method")


admin.site.register(OperatingSystem)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(PackageManager)
admin.site.register(InstallationInfo, InstallationInfoAdmin)
