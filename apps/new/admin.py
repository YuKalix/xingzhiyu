from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    readonly_fields = ('new_image_url',)
    list_display = ['title', 'read_num', 'classify','is_top', 'add_time','is_delete', 'new_image_url']
    list_filter = ['classify', 'is_top', 'is_delete', 'add_time']