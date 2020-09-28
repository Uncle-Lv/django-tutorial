"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views
from demo import db_operation
from demo.views import form, submit_form, submit_succeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('db/', db_operation.save_student_info),    # 向数据库中添加数据
    path('form/',form),
    path('form/get_info/', submit_form),
    path('submit_succeed/', submit_succeed),
    path('get_student_info/',db_operation.get_student_info),
    path('update/', db_operation.update_student_info)
]
