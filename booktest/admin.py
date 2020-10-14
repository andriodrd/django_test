from django.contrib import admin
from booktest.models import *
# admin.py文件跟网站的后台管理相关。
# Register your models here.
# 1.管理界面本地化
# 2.创建管理员

# 子类StackedInline：以块的形式嵌入
class BookInfoStackInline(admin.StackedInline):
    model = HeroInfo
    extra = 0 # 额外增加两个子对象

# 子类TabularInline：以表格的形式嵌入
class BookInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 0 # 额外增加两个子对象

# 3.自定义管理页面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']  # 修改展示的列表目录字段且列头可以进行升序或降序排列
    list_per_page = 10  # 页大小
    # 顶部和底部的显示属性
    actions_on_top = False
    actions_on_bottom = True
    # 列过滤
    list_filter = ['btitle']
    # 搜索
    search_fields = ['btitle']

    # 编辑页显示字段顺序
    # fields = ['bpub_date','btitle']

    # 分组显示
    fieldsets = (
        ('基本',{'fields':['bpub_date']}),
        ('高级',{'fields':['btitle']}),
    )
    # 已块的形式嵌入
    # inlines = [BookInfoStackInline]

    # 已块的形式嵌入
    inlines = [BookInfoTabularInline]



class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook_id']

# 4.注册模型类
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)



