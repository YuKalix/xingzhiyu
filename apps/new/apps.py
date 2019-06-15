from django.apps import AppConfig


class NewConfig(AppConfig):
    name = 'apps.new'
    # 给注册的app后台设置中文名
    verbose_name = '新闻动态'
    # 后台首页排序0
    main_menu_index = 1
