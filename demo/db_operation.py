from django.http import HttpResponse
from django.shortcuts import render

from . import models


# 向数据库中添加数据
def save_student_info(request):
    student = models.Student(name="张三")
    student.save()                                  # save() 函数，相当于SQL中的INSERT
    return HttpResponse('<p>数据添加成功！</p>')


# 获取数据
def get_student_info(request):
    # 通过 objects 模型管理器的 all() 获得所有数据行，相当于 SQL中的 SELECT * FROM
    all_student = models.Student.objects.all()

    # filter 相当于 SQL中的 WHERE，可设置条件过滤结果
    filter_student = models.Student.objects.filter(name='李四')

    # 获取单个对象
    single_student = models.Student.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2
    limit_student = models.Student.objects.order_by('name')[0:2]

    # 数据排序
    order_student = models.Student.objects.order_by("id")

    # 上面的方法可以组合使用
    order_filter_student = models.Student.objects.filter(name='张三').order_by('id')

    context = {'all': all_student, 'filter': filter_student, 'single': single_student,
               'limit': limit_student, 'order': order_student, 'order_filter': order_filter_student}

    return render(request, 'student.html', context)


"""
# 更新数据
def update_student_info(request):
    # 修改 id=1 的 name 字段，然后 save ，相当于 SQL 中的 update
    student = models.Student.objects.get(id=1)
    student.name = '李四'
    # 使用 save() 修改
    student.save()
    return HttpResponse('<p>数据更新成功！</p>')
"""


# 更新数据
def update_student_info(request):
    # 修改所有行
    models.Student.objects.all().update(name='张三')
    return HttpResponse('<p>数据更新成功！</p>')


# 删除数据
def delete_student_info(request):
    # 删除 id 为 1 的行
    student = models.Student.objects.get(id=1)
    student.delete()

    # 使用过滤器删除
    # Student.objects.filter(id=1).delete()

    # 删除所有数据
    # Student.objects.all().delete()

    return HttpResponse('<p>数据删除成功！</p>')
