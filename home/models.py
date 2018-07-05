# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

# 客户关怀表
class CustomerCare(models.Model):
    care_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('CustomerInfo', models.DO_NOTHING, blank=True, null=True)
    care_theme = models.CharField(max_length=50, blank=True, null=True)
    care_way = models.CharField(max_length=50, blank=True, null=True)
    care_time = models.DateTimeField()
    care_remark = models.CharField(max_length=1000, blank=True, null=True)
    care_nexttime = models.DateTimeField()
    care_people = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_care'

# 客户信息表
class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True)
    status = models.ForeignKey('CustomerStatus', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('CustomerSource', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('CustomerType', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_sex = models.CharField(max_length=10, blank=True, null=True)
    customer_mobile = models.CharField(max_length=20, blank=True, null=True)
    customer_qq = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=500, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_remark = models.CharField(max_length=1000, blank=True, null=True)
    customer_job = models.CharField(max_length=100, blank=True, null=True)
    customer_blog = models.CharField(max_length=100, blank=True, null=True)
    customer_tel = models.CharField(max_length=20, blank=True, null=True)
    customer_msn = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.DateTimeField()
    customer_addtime = models.DateTimeField()
    customer_addman = models.CharField(max_length=50, blank=True, null=True)
    customer_changtime = models.DateTimeField()
    change_man = models.CharField(max_length=20, blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return 'CustomerInfo:%s' %self.status

    class Meta:
        managed = False
        db_table = 'customer_info'

# 客户联系人
class CustomerLinkman(models.Model):
    linkman_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    linkman_name = models.CharField(max_length=50, blank=True, null=True)
    linkman_sex = models.CharField(max_length=20, blank=True, null=True)
    linkman_job = models.CharField(max_length=100, blank=True, null=True)
    linkman_mobile = models.CharField(max_length=20, blank=True, null=True)
    linkman_age = models.IntegerField(blank=True, null=True)
    linkman_relation = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_linkman'

# 客户预定
class CustomerLinkreord(models.Model):
    record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    link_time = models.DateTimeField()
    who_link = models.CharField(max_length=50, blank=True, null=True)
    link_type = models.CharField(max_length=50, blank=True, null=True)
    link_theme = models.CharField(max_length=200, blank=True, null=True)
    link_nexttime = models.DateTimeField()
    link_remark = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_linkreord'

# 客户来源
class CustomerSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return u'CustomerSource:%s'%self.source_name

    class Meta:
        managed = False
        db_table = 'customer_source'

# 客户状态
class CustomerStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, blank=True, null=True)
    status_explain = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return 'CustomerStatus:%s' %self.status_name
    class Meta:
        managed = False
        db_table = 'customer_status'

# 客户类型
class CustomerType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_type'

# 所属部门
class DepartmentInfo(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50, blank=True, null=True)
    department_desc = models.CharField(max_length=500, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return u'DepartmentInfo:%s' %self.is_used

    class Meta:
        managed = False
        db_table = 'department_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

# 邮箱
class EmailInfo(models.Model):
    email_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    email_content = models.CharField(max_length=2000, blank=True, null=True)
    email_time = models.DateTimeField()
    email_state = models.CharField(max_length=50, blank=True, null=True)
    email_theme = models.CharField(max_length=200, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_info'

# 房屋信息
class HouseInfo(models.Model):
    house_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('HouseType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    house_address = models.CharField(max_length=500, blank=True, null=True)
    house_price = models.IntegerField(blank=True, null=True)
    house_ambient = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_info'

# 房屋类型
class HouseType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_type'

# 公告信息
class NoticeInfo(models.Model):
    notice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    notice_item = models.CharField(max_length=100, blank=True, null=True)
    notice_content = models.CharField(max_length=2000, blank=True, null=True)
    notice_time = models.DateTimeField()
    notice_endtime = models.DateTimeField()
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice_info'

# 员工信息
class UserInfo(models.Model):
    # id
    user_id = models.AutoField(primary_key=True)
    # 部门
    department = models.ForeignKey(DepartmentInfo, models.DO_NOTHING, blank=True, null=True)
    # 角色
    role = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True)
    # 姓名
    user_name = models.CharField(max_length=50, blank=True, null=True)
    # 性别
    user_sex = models.CharField(max_length=10, blank=True, null=True)
    # 手机
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    # 年龄
    user_age = models.IntegerField(blank=True, null=True)
    # 地址
    user_address = models.CharField(max_length=500, blank=True, null=True)
    # 账号
    user_num = models.CharField(max_length=100, blank=True, null=True)
    # 密码
    user_pw = models.CharField(max_length=50, blank=True, null=True)
    user_tel = models.CharField(max_length=20, blank=True, null=True)
    # 身份证
    user_idnum = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)

    user_addtime = models.DateTimeField()
    # 用户名
    user_addman = models.CharField(max_length=50, blank=True, null=True)
    user_changetime = models.DateTimeField()
    user_changeman = models.CharField(max_length=50, blank=True, null=True)
    user_intest = models.CharField(max_length=1000, blank=True, null=True)
    user_diploma = models.CharField(max_length=20, blank=True, null=True)
    # 工资卡
    user_bankcard = models.CharField(max_length=20, blank=True, null=True)
    # 民族
    user_nation = models.CharField(max_length=20, blank=True, null=True)
    # 婚姻
    is_married = models.CharField(max_length=10, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'

#添加角色
class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, blank=True, null=True)
    role_power = models.IntegerField(blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'
