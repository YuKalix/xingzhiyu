from django.apps import AppConfig


class SuccessCaseConfig(AppConfig):
    name = 'apps.success_case'
    # 给注册的app后台设置中文名
    verbose_name = '成功案例'
    # 后台首页排序0
    main_menu_index = 0

