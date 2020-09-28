from django.shortcuts import render, redirect

# Create your views here.


# 返回表单页面
def form(request):
    return render(request, 'form.html')


"""
# 表单处理函数
def submit_form(request):
    request.encoding = 'utf-8'  # 设置编码为 utf-8
    message = request.GET['message']  # 获取名为 message 的表单数据
    print('GET: ' + message)

    # 表单提交后重定向到提示页面
    return redirect('/submit_succeed')
"""


# 表单处理函数
def submit_form(request):
    request.encoding = 'utf-8'  # 设置编码为 utf-8
    message = request.POST['message']  # 获取名为 message 的表单数据
    print('POST: ' + message)

    # 表单提交后重定向到提示页面
    return redirect('/submit_succeed')


def submit_succeed(request):
    return render(request, 'submit_succeed.html')
