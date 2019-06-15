from django.apps import AppConfig


class IndexConfig(AppConfig):
    # 注册的app
    name = 'apps.index'
    # 给注册的app后台设置中文名
    verbose_name = '首页设置'
    # 后台首页排序0
    main_menu_index = 1