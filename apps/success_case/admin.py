from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Case)
class LogoAdmin(admin.ModelAdmin):
    readonly_fields = ('case_image_url',)
    list_display = ['describe', 'case_image_url', 'url', 'is_display', 'add_time']
