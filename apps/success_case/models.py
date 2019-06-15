from datetime import datetime

from django.db import models
from django.utils.html import format_html
# Create your models here.


# 案例
class Case(models.Model):
    image = models.ImageField(max_length=200, upload_to='success_case/%Y/%m', verbose_name='展示图')
    describe = models.CharField(verbose_name='案列简介', max_length=50, default='')
    url = models.URLField(verbose_name='案例链接')
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())
    is_display = models.BooleanField(verbose_name='是否展示', default=True)

    def case_image_url(self):
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    case_image_url.short_description = u'封面'

    class Meta:
        verbose_name = '案例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.describe