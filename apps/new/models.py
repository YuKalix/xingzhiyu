from datetime import datetime

from django.db import models
from django.utils.html import format_html

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


# 新闻
class New(models.Model):
    CLASSIFYS = (
        ('announcement', '网站公告'),
        ('industry_information', '行业资讯'),
        ('media_report', '媒体报道'),
    )
    classify = models.CharField(verbose_name='文章分类', choices=CLASSIFYS, max_length=36)
    image = models.ImageField(max_length=200, upload_to='new/%Y/%m', verbose_name='封面')
    title = models.CharField(verbose_name='文章标题', max_length=64)
    author = models.CharField(verbose_name='文章作者', max_length=32, default='YuKalix')
    intro = models.CharField(verbose_name='文章简介', max_length=300, default='')
    content = RichTextUploadingField(verbose_name='文章内容', default='')
    read_num = models.PositiveIntegerField(verbose_name='文章数量', default=0)
    add_time = models.DateTimeField(verbose_name='时间', auto_now_add=datetime.now())
    is_top = models.BooleanField(verbose_name='是否置顶(首页)', default=False)
    is_delete = models.BooleanField(verbose_name='是否展示', default=True)

    def new_image_url(self):
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    new_image_url.short_description = u'封面'

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title