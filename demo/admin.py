from django.contrib import admin
from . import models


# Register your models here.
# admin.site.register(models.Student)  # 注册模型

admin.site.site_header = '自定义后台管理'
admin.site.site_title = '自定义标题'


@admin.register(models.Student)  # 装饰器注册模型
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']  # 设置在后台显示的字段
    readonly_fields = ['name']  # 设置只读字段

