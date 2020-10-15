from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *
# views.py文件跟接收浏览器请求，进行处理，返回页面相关。
# Create your views here.

# /index
def index(request):
    '''首页，展示所有图书'''
    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传递到模板中，然后渲染模板s
    context = {'booklist': booklist}
    return render(request, 'booktest/index.html', context)

# /detail
def detail(request,bid):
    '''详情页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示'''
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    context = {'book': book, 'heros': heros}
    return render(request,'booktest\detail.html', context)