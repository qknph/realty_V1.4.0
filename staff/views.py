# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import *

# Create your views here.
def emp_list(request):
    return render(request, 'emp_list.html')

# 房屋信息
def house_list(request):
    houseinfo = HouseInfo.objects.all()
    return render(request, 'house_list.html',{"houseinfo":houseinfo})

# 房屋类型
def house_type_list(request):
    housetype = HouseType.objects.all()
    # return render(request, 'Toh.html', {'housetype': housetype})
    return render(request, 'house_type_list.html',{'housetype': housetype})

# 部门信息
def dept_list(request):
    department = DepartmentInfo.objects.all()
    # return render(request, 'Dept.html', {'department': department})
    return render(request, 'dept_list.html',{'department': department})


def notice_list(request):
    return render(request, 'notice_list.html')


# 删除房屋类型操作
def house_type_delete(request):
    print "fangwu"
    cno = request.GET.get('cno', '')
    cn = int(cno)
    HouseType.objects.filter(type_id=cn).delete()
    return HttpResponseRedirect('/staff/house_type_list.html')

#删除部门信息操作
def d_del_view(request):
    print 'sdlkflkjls'
    #获取部门信息
    dell = request.GET.get('dell','0')
    print dell
    dell = int(dell)
    DepartmentInfo.objects.filter(department_id= dell).delete()
    return HttpResponseRedirect('/staff/Dedept_list.html/')
