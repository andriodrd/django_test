from django.db import models
# models.py文件跟数据库操作相关
# 1.在models.py中定义模型类
# 2.迁移
# 3.通过类和对象完成数据增删改查操作
# Create your models here.
# 定义模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()  # 参数同DatetimeField和TimeField
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除 false==0

    # 修改列的属性
    def Btitle(self):
        return self.btitle
    Btitle.short_description = '书名'
    # 自定义的列添加排序按钮
    Btitle.admin_order_field = 'btitle'
    # 中文标题
    btitle = models.CharField('标题',max_length=30)
    bpub_date = models.CharField('出版日期',max_length=30)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcomment = models.CharField(max_length=200)  # 英雄描述信息
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)  # django2.0后外键(ForeignKey)和一对一(OneToOneField)加上on_delete=models.CASCADE这个字段
