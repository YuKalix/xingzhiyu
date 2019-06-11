from datetime import datetime

from django.db import models
from django.utils.html import format_html

# Create your models here.

# 网站整体配置信息
# 用于后期可能把它作为一个模版多次,不同对象使用
# 企业信息
class Information(models.Model):
    name = models.CharField(max_length=36, blank=True, verbose_name='企业名称', default='星之羽网络科技有限公司')
    introduce = models.TextField(max_length=360, blank=True, verbose_name='企业描述', default='')
    address = models.CharField(max_length=72, blank=True, verbose_name='企业地址', default='')
    mobile =models.CharField(max_length=12, blank=True, verbose_name='企业电话', default='')
    qq = models.CharField(max_length=12, blank=True, verbose_name='企业QQ', default='')
    email = models.EmailField(blank=True, verbose_name='企业邮箱', default='admin@admin.admin')
    icp = models.CharField(max_length=100, blank=True, verbose_name='企业备案号', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(verbose_name='是否使用', default=True)

    class Meta:
        verbose_name = '企业信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 首页logo
class Logo(models.Model):
    image = models.ImageField(max_length=200, upload_to='logo/%Y')
    describe = models.CharField(max_length=50, verbose_name='logo描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def logo_image_url(self):
        print(self.image)
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    logo_image_url.short_description = u'图片'

    class Meta:
        verbose_name = '首页logo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.describe


# banner
class Banner(models.Model):
    image = models.ImageField(max_length=200, upload_to='banner/%Y')
    describe = models.CharField(max_length=50, verbose_name='banner描述')
    url = models.URLField(verbose_name='banner链接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def banner_image_url(self):
        print(self.image)
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    banner_image_url.short_description = u'图片'

    class Meta:
        verbose_name = '首页banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.describe


# 我们的服务
class Service(models.Model):
    image = models.ImageField(max_length=200, upload_to='service/%Y')
    describe = models.CharField(max_length=50, verbose_name='service描述')
    url = models.CharField(max_length=100, verbose_name='service链接', default='#serve')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(verbose_name='是否使用', default=True)

    def service_image_url(self):
        print(self.image)
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    service_image_url.short_description = u'图片'

    class Meta:
        verbose_name = '我们的服务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.describe


# 我们的团队
class Team(models.Model):
    photo = models.ImageField(max_length=200, upload_to='team/%Y')
    name = models.CharField(max_length=16, verbose_name='姓名')
    introduce = models.TextField(max_length=160, verbose_name='介绍')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(verbose_name='是否在职', default=True)

    def team_photo_url(self):
        return format_html( '<img src="{0}" width="100px"/>', self.photo.url)
    team_photo_url.short_description = u'照片'

    class Meta:
        verbose_name = '我们的团队'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 合作伙伴
class Partner(models.Model):
    image = models.ImageField(max_length=200, upload_to='partner/%Y')
    name = models.CharField(max_length=16, verbose_name='企业名称')
    introduce = models.TextField(max_length=160, verbose_name='介绍')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_delete = models.BooleanField(verbose_name='是否合作', default=True)

    def partner_image_url(self):
        return format_html( '<img src="{0}" width="100px"/>', self.image.url)
    partner_image_url.short_description = u'照片'

    class Meta:
        verbose_name = '合作伙伴'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
