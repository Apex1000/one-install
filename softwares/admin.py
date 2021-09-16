from django.contrib import admin
from softwares.models import (
    InstallationMethod,
    Software,
    InstallationInfo
)
# Register your models here.


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linux', 'mac_OS', 'windows')
    search_fields = ('name',)
    list_filter = ('linux', 'mac_OS', 'windows')


class InstallationInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'software', 'method')


admin.site.register(Software, SoftwareAdmin)
admin.site.register(InstallationMethod)
admin.site.register(InstallationInfo, InstallationInfoAdmin)
