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
    count = HouseInfo.objects.count()
    print count
    return render(request, 'house_list.html',{"houseinfo":houseinfo,'count':count})

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
    note = NoticeInfo.objects.all()
    return render(request, 'notice_list.html',{'note':note})


def note_del(request):
    dele = request.GET.get('dele','')
    dele = int(dele)
    NoticeInfo.objects.filter(notice_id=dele).delete()

    return HttpResponseRedirect('/staff/notice_list.html')


# 删除房屋类型操作
def house_type_delete(request):
    cno = request.GET.get('cno', '')
    cn = int(cno)
    HouseType.objects.filter(type_id=cn).delete()
    return HttpResponseRedirect('/staff/house_type_list.html')

#删除部门信息操作
def d_del_view(request):
    #获取部门信息
    dell = request.GET.get('dell','')
    dell = int(dell)
    DepartmentInfo.objects.filter(department_id= dell).delete()
    return HttpResponseRedirect('/staff/Dedept_list.html/')

#删除房屋信息
def E_del_view(request):
    cno = request.GET.get('cno', '')
    cn = int(cno)
    HouseInfo.objects.filter(house_id= cn).delete()
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

# 查询房屋信息
def query_house(request):
    houseinput = request.POST.get('houseInput','')
    queryType = request.POST.get('queryType','')
    if queryType == '1':
        house = HouseType.objects.get(type_name__contains=houseinput).houseinfo_set.all()
        return render(request, 'house_list.html', {'houseinfo':house})
    elif queryType == '2':
        house = HouseInfo.objects.filter(house_address__contains=houseinput)
        return render(request,'house_list.html',{'houseinfo':house})

# 房屋类型查询
def query_house_type(request):
    housetypename = request.POST.get('houseTypeName','')
    types = HouseType.objects.filter(type_name__contains=housetypename)
    return render(request,'house_type_list.html',{'housetype':types})

# 部门信息查询
def query_dept(request):
    departmentname = request.POST.get('departmentName','')
    dept = DepartmentInfo.objects.filter(department_name__contains=departmentname)
    return render(request,'dept_list.html',{'department':dept})

# 公告信息查询
def query_note(request):
    querytype = request.POST.get('queryType','')
    noticeinput = request.POST.get('noticeInput','')
    if querytype == '1':
        item = NoticeInfo.objects.filter(notice_item__contains=noticeinput)
        return render(request,"notice_list.html",{'note':item})
    elif querytype == '2':
        con = NoticeInfo.objects.filter(notice_content__contains=noticeinput)
        return render(request,'notice_list.html',{'note':con})

    return None


def note_add(request):
    return HttpResponse('zanwu')