from django.db import models

# Create your models here.


# 继承 models.Model 类
class Student(models.Model):
    # CharField 相当于 varchar，max_length 参数限定长度
    name = models.CharField(max_length=20, verbose_name='名字')

    class Meta:
        db_table = 'student'  # 自定义数据库表名
