from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# 由于设计初失误,emmmm还得稍微引入
from apps.index.models import Information,Logo

class Safe(View):
    def get(self, request):
        # 获取信息
        information = Information.objects.first()
        # 获取logo
        logo = Logo.objects.first()


        return render(request, 'safe.html', {
            'information': information,
            'logo': logo,
        })
