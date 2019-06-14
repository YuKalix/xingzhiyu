from django.contrib import admin

# Register your models here.

from .models import *

# 配置后台基本设置
# 设置base_site.html的Footer
admin.site.site_header = '星之羽后台管理'
# 设置base_site.html的Title
admin.site.site_title = '星之羽后台管理'
# 设置base_site.html的Footer
admin.site.site_footer = 'YuKalix小小窝'

admin.site.index_title = '星之羽后台管理'

@admin.register(Information)
class InformaticaAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ['name', 'icp', 'add_time', 'is_delete']

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ('logo_image_url',)
    list_display = ['describe', 'logo_image_url']

@admin.register(Banner)
class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ('banner_image_url',)
    list_display = ['describe', 'url', 'banner_image_url']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('service_image_url',)
    list_display = ['describe', 'url', 'service_image_url']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('team_photo_url',)
    list_display = ['name', 'introduce', 'team_photo_url', 'is_delete']

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    readonly_fields = ('partner_image_url',)
    list_display = ['name', 'introduce', 'partner_image_url', 'is_delete']