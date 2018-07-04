# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
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

#删除房屋信息
def E_del_view(request):
    cno = request.GET.get('cno', '')
    cn = int(cno)
    HouseInfo.objects.filter(houseinfo__house_id= cn).delete()
    return HttpResponseRedirect('/staff/house_list.html/')


# 编辑房屋信息#
def Ed_view(request):
    if request.method == 'GET':
        # 获取该房屋信息信息
        cno = request.GET.get('cno', '')
        cno = int(cno)
        ed = HouseInfo.objects.filter(house_id=cno)
        return render(request, 'house_edit.html', {'ed': ed})
    else:
        # 获取页面中内容
        # input_ADDRESS = request.POST.get('input_ADDRESS','fffffffff')
        # print input_ADDRESS

        return HttpResponse('chaxunchenggong')


def query_house(request):
    houseinput = request.POST.get('houseInput','')
    queryType = request.POST.get('queryType','')
    if queryType == '1':
        house = HouseType.objects.get(type_name=houseinput).houseinfo_set.all()
        return render(request, 'house_list.html', {'houseinfo':house})
    elif queryType == '2':
        house = HouseInfo.objects.filter(house_address=houseinput)
        return render(request,'house_list.html',{'houseinfo':house})