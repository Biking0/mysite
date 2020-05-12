from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


# 创建模型类
class Meishi(models.Model):
    id = models.AutoField(primary_key=True)  # 该字段可以不写，它会自动补全
    food_name = models.CharField(max_length=30)  # 设置食物名称
    food_author = models.CharField(max_length=8)  # 设置食物制作人
    food_money = models.FloatField()  # 设置食物价格
    food_star = models.CharField(max_length=10, default='普通')  # 设置食物美味程度

    def __str__(self):  # 重写直接输出类的方法
        return "<Meishi:{id=%s,food_name=%s,food_author=%s,food_money=%s,food_star=%s}>" \
               % (self.id, self.food_name, self.food_author, self.food_money, self.food_star)


# 创建模型类
class Meishi1(models.Model):
    id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=30)
    food_author = models.CharField(max_length=8)
    food_money = models.FloatField()  # 设置食物价格
    food_star = models.CharField(max_length=10, default='普通')  # 设置食物美味程度

    def __str__(self):  # 重写直接输出类的方法
        return "<Meishi1:{id=%s,food_name=%s,food_author=%s,food_money=%s,food_star=%s}>" \
               % (self.id, self.food_name, self.food_author, self.food_money, self.food_star)

# 招投标公告信息模型
class tender_info(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    view_cont = models.CharField(max_length=100)
    release_time = models.CharField(max_length=100)
    url = models.CharField(max_length=300, null=True)

    def __str__(self):  # 重写直接输出类的方法
        return "<tender_info:{name=%s,company=%s,view_cont=%s,release_time=%s,url=%s}>" \
               % (self.name, self.company, self.view_cont, self.release_time, self.url)
