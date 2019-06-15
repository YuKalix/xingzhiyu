from django.shortcuts import render
from django.views.generic import View


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Case
# 由于设计初失误,emmmm还得稍微引入
from apps.index.models import Information,Logo

class SuccessCase(View):
    def get(self, request):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()

        # 获取案例
        cases = Case.objects.filter(is_display=True).order_by('-add_time')
        new_caases = cases[:8]
        # 分页
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        # # 这里指从中取五个出来，每页显示5个
        # p = Paginator(cases, 1)
        # cases = p.page(page)


        return render(request, 'success_case.html', {
            'information': information,
            'logo': logo,
            'new_caases': new_caases,
            'cases': cases,
        })
