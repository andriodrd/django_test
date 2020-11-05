from django.shortcuts import render,redirect
from django.http import HttpResponse
from booktest.models import *
# views.py文件跟接收浏览器请求，进行处理，返回页面相关。
# Create your views here.
# 字段查询
    # filter()
        # 1) 查询等exact  list=BookInfo.objects.filter(id__exact=1) 等价为 list=BookInfo.objects.filter(id=1)
        # 2) 模糊查询
             # contains：是否包含 -- list = BookInfo.objects.filter(btitle__contains='传')
             # startswith、endswith：以指定值开头或结尾 list = BookInfo.objects.filter(btitle__endswith='部')
             # 以上运算符都区分大小写，在这些运算符前加上i表示不区分大小写，如iexact、icontains、istartswith、iendswith.
        # 3) 空查询
             # isnull：是否为null -- list = BookInfo.objects.filter(btitle__isnull=False)
        # 4) 范围查询
             #  in：是否包含在范围内--list = BookInfo.objects.filter(id__in=[1, 3, 5])
        # 5) 比较查询
             #  gt、gte、lt、lte：大于、大于等于、小于、小于等于。：是否包含在范围内--list = BookInfo.objects.filter(id__in=[1, 3, 5])
        # 6) 日期查询
             #  year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算--list = BookInfo.objects.filter(id__in=[1, 3, 5])
    # exclude()
             #  不等于的运算符，使用exclude()过滤器。
    # get()


# 登录装饰器
def login_required(func):
    '''登录装饰器页面'''
    def close(request, *args, **kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            return func(request, *args, **kwargs)
        else:
            # 用户未登录，跳转至登录页
            return redirect('/login')
    return close


# /login
def login(request):
    '''登录页面'''
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        context = {'username': username}
        return render(request, 'booktest\login.html', context)




# /login_check
def login_check(request):
    '''登录检验页面'''
    # request.POST 保存的是post方式提交的参数 QueryDict
    # request.GET 保存的是get方式提交的参数\
    # 1.获取用户名,实际开发根据用户名和密码查找数据库进行验证

    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')

    # 2.进行登录的验证，模拟
    if username == 'admin' and password == 'admin':
        # 跳转到首页
        response = redirect('/index')
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
        request.session['islogin'] = True
        return response
    else:
        # 跳转到登录页面
        return redirect('/login')


# /index
@login_required  # 增加装饰器
def index(request):
    '''首页，展示所有图书'''
    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传递到模板中，然后渲染模板
    context = {'booklist': booklist}
    return render(request, 'booktest/index.html', context)

# /detail
@login_required
def detail(request,bid):
    '''详情页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示'''
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    context = {'book': book, 'heros': heros}
    return render(request,'booktest\detail.html', context)