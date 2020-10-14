from django.db import models
# models.py文件跟数据库操作相关
# 1.在models.py中定义模型类
# 2.迁移
# 3.通过类和对象完成数据增删改查操作
# Create your models here.
# 定义模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()  # 参数同DateField和TimeField
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
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE) # django2.0后外键(ForeignKey)和一对一(OneToOneField)加上on_delete=models.CASCADE这个字段
