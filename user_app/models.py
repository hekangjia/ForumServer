#coding=utf-8
from django.db import models
from django.contrib.auth.models import User, make_password, check_password, Group, GroupManager
from django.contrib.auth.admin import UserAdmin
from ForumServer.settings import UPLOADTO

# Create your models here.
class ProfileBase(type):                    #对于传统类，他们的元类都是types.ClassType
    def __new__(cls, name, bases, attrs):      #带参数的构造器，__new__一般用于设置不变数据类型的子类
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

class ProfileUser(object):
    __metaclass__ = ProfileBase     #类属性


# 扩充django的user表字段
class MyProfile(ProfileUser):
    headImage = models.ImageField(upload_to=UPLOADTO, null=True, blank=True, verbose_name="头像", help_text="头像可以不上传，会有默认头像")
    is_manager = models.BooleanField(default=False, verbose_name="是否为管理员")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")