from django.shortcuts import render
from django.views.generic import View

from .models import *
# Create your views here.


# 首页
class Index(View):
    def get(self,request):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()
        # 获取banner
        banners = Banner.objects.all()[:4]
        # 我们的服务
        services = Service.objects.filter(is_delete=True)
        # 我们的团队
        team = Team.objects.filter(is_delete=True)
        # 合作伙伴
        partners = Partner.objects.filter(is_delete=True)



        return  render(request, 'index.html',{
            'information': information,
            'logo': logo,
            'banners': banners,
            'services': services,
            'team': team,
            'partners': partners,
        })