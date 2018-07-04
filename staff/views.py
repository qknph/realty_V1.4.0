# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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