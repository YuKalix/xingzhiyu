from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import *

# 由于设计初失误,emmmm还得稍微引入
from apps.index.models import Information,Logo


# 新闻列表
class NewList(View):
    def get(self, request):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()


        # 获取所有classify
        classifies = New.CLASSIFYS
        # 取到的是元组,序列化成dict
        classifies = dict(classifies)

        # 获取新闻
        # 获取当前页面文章类别
        classify = request.GET.get('classify', '')
        print(classify)
        if classify:
            news = New.objects.filter(classify=classify, is_delete=True)
        else:
            news = New.objects.all().filter(is_delete=True)


        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(news, 2)
        news = p.page(page)



        return render(request, 'new_list.html', {
            'information': information,
            'logo': logo,

            'classifies':classifies,
            'news': news,
        })


# 文章
class NewArticle(View):
    def get(self, request, classify, new_id):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()

        # 获取点击文章
        article = New.objects.filter(id=new_id)
        return render(request, 'new.html', {
            'information': information,
            'logo': logo,

            'article': article[0],
        })
