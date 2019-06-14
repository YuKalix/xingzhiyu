from django.shortcuts import render
from django.views.generic import View

from .models import *
# Create your views here.
from apps.new.models import New


# 首页
class Index(View):
    def get(self,request):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()
        # 获取banner
        banners = Banner.objects.all()[:4]
        # 最新公告
        announcements = New.objects.filter(classify='announcement')[:3]
        # 我们的服务
        services = Service.objects.filter(is_delete=True)
        # 咨询中心
        news = New.objects.filter(is_top=True).order_by('-add_time')[:7]
        # 我们的团队
        team = Team.objects.filter(is_delete=True)
        # 合作伙伴
        partners = Partner.objects.filter(is_delete=True)



        return  render(request, 'index.html',{
            'information': information,
            'logo': logo,
            'banners': banners,
            'announcements': announcements,
            'services': services,
            'news': news,
            'team': team,
            'partners': partners,
        })