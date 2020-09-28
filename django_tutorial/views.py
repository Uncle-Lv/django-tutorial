from django.http import HttpResponse
from django.shortcuts import render


"""
def hello(request):
    return HttpResponse("Hello Django!")
"""


def hello(request):
    # 创建一个字典，其中键值对和模板页面中的插值表达式对应
    context = {'message': '这个是一个 Django 模板!'}
    return render(request, 'hello.html', context)